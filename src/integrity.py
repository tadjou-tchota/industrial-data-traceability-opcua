"""
Auteur : TCHOTA Tadjou
Description : Module de hachage cryptographique SHA-256 pour l'intégrité des données.
"""

import hashlib
import json

def compute_integrity_hash(payload):
    """Génère un hash SHA-256 pour garantir l'intégrité cryptographique du message."""
    payload_string = json.dumps(payload, sort_keys=True)
    return hashlib.sha256(payload_string.encode('utf-8')).hexdigest()
