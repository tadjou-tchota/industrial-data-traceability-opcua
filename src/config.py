"""
Auteur : TCHOTA Tadjou
Description : Paramètres de configuration du pipeline IIoT.
"""

OPCUA_SERVER_URL = "opc.tcp://localhost:4840/freeopcua/server/"
OPCUA_SERVER_ENDPOINT = "opc.tcp://0.0.0.0:4840/freeopcua/server/"
NODE_ID = "ns=2;i=2"
DB_NAME = "pipeline_industrial.db"

PROVENANCE_INFO = {
    "gateway_id": "GW-LINE-01",
    "operator": "TCHOTA Tadjou",
    "version": "1.0.0"
}
