"""
Auteur : TCHOTA Tadjou
Description : Serveur OPC UA simulant un capteur industriel avec injection de statuts Good/Bad.
"""

import time
from opcua import Server, ua
from config import OPCUA_SERVER_ENDPOINT

def run_server():
    server = Server()
    server.set_endpoint(OPCUA_SERVER_ENDPOINT)

    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    objects = server.get_objects_node()
    furnace = objects.add_object(idx, "FourIndus")
    temperature_var = furnace.add_variable(idx, "Temperature", 22.5)
    temperature_var.set_writable()

    server.start()
    print("[SERVEUR] Serveur OPC UA démarré sur le port 4840...")
    print("[SERVEUR] Auteur : TCHOTA Tadjou")
    print("[SERVEUR] Simulation avec injection de statuts 'Good' et 'Bad' en cours...")

    try:
        count = 20.0
        counter = 0
        while True:
            count += 0.5
            counter += 1

            dv = ua.DataValue()
            dv.Value = ua.Variant(count, ua.VariantType.Double)
            
            # Simulation d'une panne / perte de données toutes les 4 itérations
            if counter % 4 == 0:
                dv.StatusCode = ua.StatusCode(ua.StatusCodes.BadDataLost)
                print(f"[SERVEUR] -> Injection d'un statut BAD pour la valeur {count}")
            else:
                dv.StatusCode = ua.StatusCode(ua.StatusCodes.Good)

            temperature_var.set_value(dv)
            time.sleep(2)
            
    except KeyboardInterrupt:
        server.stop()
        print("[SERVEUR] Arrêt du serveur.")

if __name__ == "__main__":
    run_server()
