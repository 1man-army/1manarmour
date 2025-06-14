"""
Voice Router - Professor&Master Memorable
Routes operator voice commands to agent actions, supports speech-to-text, logging, and dashboard sync.
"""

from config import C2_URL, OPERATOR_ID
from datetime import datetime
import requests

def route_voice_command(cmd, sync=True):
    # In real use, integrate with speech-to-text and agent comms
    print(f"[VOICE] Routing command: {cmd}")
    log_event(f"Voice command routed: {cmd}")
    if sync:
        sync_voice_dashboard(cmd)

def sync_voice_dashboard(cmd):
    # Stub: Integrate with dashboard WebSocket or API for real-time voice command sync
    try:
        requests.post(f"{C2_URL}/dashboard/voice", data={"cmd": cmd, "operator": OPERATOR_ID})
    except Exception:
        pass

def log_event(msg):
    with open("agent.log", "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        route_voice_command(" ".join(sys.argv[1:]))
    else:
        print("Usage: python voice_router.py <command>")