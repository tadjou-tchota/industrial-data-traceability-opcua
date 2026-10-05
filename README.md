# industrial-data-traceability-opcua
Pipeline IIoT OPC UA – Industrial Data Quality, Provenance and Traceability

# Pipeline IIoT OPC UA : Assurance, Traçabilité et Intégrité des Données

Ce dépôt présente une architecture logicielle modulaire de type **Edge-to-Cloud / Passerelle IIoT** conçue pour répondre aux exigences critiques de **confiance, de traçabilité numérique et d'intégrité des données** dans les environnements industriels et les jumeaux numériques.

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
