# industrial-data-traceability-opcua
Pipeline IIoT OPC UA – Industrial Data Quality, Provenance and Traceability

Prototype expérimental développé pour simuler une chaîne industrielle de collecte, contrôle qualité, traçabilité et sécurisation des données.

Le système met en œuvre :
un serveur industriel OPC UA simulant un équipement ;
la génération de données de température ;
l'injection de statuts de qualité Good et BadDataLost ;
un client OPC UA assurant la collecte continue ;
le contrôle de la qualité des données ;
la traçabilité de la provenance ;
l'horodatage des acquisitions ;
le calcul d'une empreinte SHA-256 ;
la persistance des données dans SQLite ;
la conservation des événements normaux et des anomalies.

Ce prototype constitue une première expérimentation autour des problématiques de qualité, intégrité, provenance et traçabilité des données industrielles, avec une perspective d'extension vers les systèmes cyber-physiques et les jumeaux numériques.
