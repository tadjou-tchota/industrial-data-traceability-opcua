# industrial-data-traceability-opcua

# Pipeline IIoT OPC UA – Industrial Data Quality, Provenance and Traceability

Prototype expérimental développé par pour simuler une chaîne industrielle de collecte, contrôle qualité, traçabilité et sécurisation des données.

---

## 🏗️ Architecture Modulaire

Le projet est structuré de manière modulaire pour dissocier la configuration, la simulation, la sécurité cryptographique, la persistance et la logique de collecte :

* **`config.py`** : Centralise les paramètres de configuration et les métadonnées de provenance.
* **`database.py`** : Gère la création du schéma et l'insertion persistante (succès et pannes) dans SQLite.
* **`integrity.py`** : Assure la signature et l'inviolabilité des messages via un hachage SHA-256.
* **`opcua_server.py`** : Simule un équipement industriel avec injection de statuts nominaux (`Good`) et d'anomalies (`BadDataLost`).
* **`traceability_client.py`** : Assure l'écoute continue, l'évaluation dynamique de la qualité et l'archivage sécurisé.

---

## 🚀 Guide d'Utilisation

### Prérequis Techniques
* Python 3.10 ou supérieur.
* Bibliothèque Python OPC UA (`opcua`).

Installation de la dépendance :
```bash
pip install opcua

Étape 1 : Démarrer le Serveur OPC UA (Simulation)
Ouvrez un premier terminal et lancez le simulateur d'équipement :
