"""
Auteur : TCHOTA Tadjou
Description : Gestion de la base de données SQLite (initialisation et persistance).
"""

import sqlite3
from config import DB_NAME

def init_database():
    """Initialise la base de données SQLite locale."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sequence INTEGER,
            timestamp_acquisition TEXT,
            source_timestamp TEXT,
            node_id TEXT,
            value REAL,
            quality_status TEXT,
            quality_check TEXT,
            gateway_id TEXT,
            integrity_hash TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_to_database(payload):
    """Enregistre un payload (succès ou panne) dans la base SQLite."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sensor_logs (
            sequence, timestamp_acquisition, source_timestamp, 
            node_id, value, quality_status, quality_check, 
            gateway_id, integrity_hash
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        payload["sequence"],
        payload["timestamp_acquisition"],
        payload["source_timestamp"],
        payload["node_id"],
        payload["value"],
        payload["quality_status"],
        payload["quality_check"],
        payload["provenance"]["gateway_id"],
        payload["integrity_hash"]
    ))
    conn.commit()
    conn.close()
