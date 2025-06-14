"""
AI Task Suggestion Module - CrossComPJxAI
Suggests next operator actions based on collected intel.
"""

from datetime import datetime
from cp_opereatorex.comms.comlink_ai import ComLinkAI
from core.opsec.anomaly_watchdog import AnomalyWatchdog
from core.ai.ai_task_suggest import suggest_tasks
from core.lateral.pass_the_hash import automate_lateral_movement
from core.lateral.kerberos_probe import extract_kerberos_tickets
from core.recon.recon_ai import passive_recon

com = ComLinkAI()
watchdog = AnomalyWatchdog()

def suggest_tasks(context):
    if "NTLM" in str(context):
        return ["Try pass-the-hash lateral movement.", "Dump Kerberos tickets.", "Escalate privileges."]
    if "linux" in str(context).lower():
        return ["Check for sudo/root access.", "Enumerate SSH keys.", "Scan for cron jobs."]
    return ["Run full recon.", "Check persistence.", "Monitor for anomalies."]

def log_event(msg):
    with open("agent.log", "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

if __name__ == "__main__":
    print(suggest_tasks({"platform": "Windows", "NTLM": "hash"}))