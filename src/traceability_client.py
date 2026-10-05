"""
Auteur : TCHOTA Tadjou
Description : Client OPC UA en flux continu, intégrant le contrôle de qualité, 
              la traçabilité, l'intégrité SHA-256 et la persistance SQLite.
"""

import json
import time
from datetime import datetime
from opcua import Client

from config import OPCUA_SERVER_URL, NODE_ID, PROVENANCE_INFO
from database import init_database, save_to_database
from integrity import compute_integrity_hash

def run_client():
    init_database()
    print("[BDD] Base de données SQLite initialisée.")

    client = Client(OPCUA_SERVER_URL)
    try:
        client.connect()
        print("[CLIENT] Connecté au serveur OPC UA avec succès.")
        print("[CLIENT] Auteur : TCHOTA Tadjou")

        var_node = client.get_node(NODE_ID) 

        print("\n--- Début du flux continu et sécurisé (Appuyez sur Ctrl+C pour arrêter) ---\n")
        
        sequence_id = 0
        while True:
            sequence_id += 1
            timestamp_acq = datetime.now().astimezone().isoformat()
            
            try:
                data_value = var_node.get_data_value()
                raw_value = data_value.Value.Value if data_value.Value else 0.0
                source_timestamp = str(data_value.SourceTimestamp)
                
                status_name = "Good"
                try:
                    status_code_obj = data_value.StatusCode
                    if hasattr(status_code_obj, "name"):
                        status_name = status_code_obj.name
                    else:
                        status_name = str(status_code_obj)
                except Exception:
                    status_name = "Good"

                quality_check = "PASSED" if "Good" in status_name else "FAILED"
                value_to_log = float(raw_value) if raw_value is not None else 0.0

            except Exception as read_err:
                source_timestamp = str(datetime.now().astimezone())
                status_name = "BadDataLost"
                quality_check = "FAILED"
                value_to_log = 0.0
                print(f"[ALERTE CAPTEUR] Panne détectée sur le cycle {sequence_id} : {read_err}")

            payload = {
                "sequence": sequence_id,
                "timestamp_acquisition": timestamp_acq,
                "source_timestamp": source_timestamp,
                "node_id": str(var_node.nodeid),
                "value": value_to_log,
                "quality_status": status_name,
                "quality_check": quality_check,
                "provenance": PROVENANCE_INFO
            }

            integrity_hash = compute_integrity_hash(payload)
            payload["integrity_hash"] = integrity_hash

            save_to_database(payload)

            print(json.dumps(payload, indent=4))
            print(f"-> [Statut: {status_name}] Séquence {sequence_id} enregistrée en BDD.")
            print("-" * 50)
            
            time.sleep(2)

    except KeyboardInterrupt:
        print("\n[CLIENT] Arrêt demandé par l'utilisateur (Ctrl+C).")
    except Exception as e:
        print(f"[ERREUR CLIENT CRITIQUE] {e}")
    finally:
        client.disconnect()
        print("[CLIENT] Déconnecté du serveur.")

if __name__ == "__main__":
    run_client()
