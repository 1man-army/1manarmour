# config.py

import os

# OPERATOR CONFIG
OPERATOR_ID = "QuantumAI"         # Ya apna operator ID

# LOGGING
LOG_DIR = os.path.join(os.getcwd(), "logs")
HUD_LOG = os.path.join(LOG_DIR, "hud_log.json")
ANOMALY_LOG = os.path.join(LOG_DIR, "anomalies.log")

# OPERATION MODES
DEFAULT_MODE = "stealth"

# C2 SETTINGS (dummy IP for testing)
C2_HOST = "127.0.0.1"
C2_PORT = 9090
C2_URL = "http://localhost:5000"  # Ya jo bhi aapka C2/dashboard URL hai

# Ensure log directory exists
def ensure_directories():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
        print(f"[+] Created log directory: {LOG_DIR}")
    else:
        print(f"[~] Log directory already exists: {LOG_DIR}")

if __name__ == "__main__":
    print("🔧 Config loaded successfully.")
    print(f"OPERATOR_ID = {OPERATOR_ID}")
    print(f"HUD_LOG = {HUD_LOG}")
    print(f"ANOMALY_LOG = {ANOMALY_LOG}")
    ensure_directories()
