# comlink_ai.py – CrossComPJxAI Operator-Agent Comm Bridge
# Manages HUD feeds, mission alerts, operator chat, logs, and AI tasking

from datetime import datetime
import json

class ComLinkAI:
    def __init__(self):
        self.hud_stream = []
        self.chat_log = []
        self.alert_log = []
        self.relay_stack = []
        self.sync_records = []

    def send_to_hud(self, payload):
        stamp = datetime.now().strftime("%H:%M:%S")
        msg = f"[HUD] [{stamp}] {payload}"
        self.hud_stream.append(msg)
        print(msg)

    def send_alert(self, msg):
        alert = f"[ALERT] {datetime.now().isoformat()} | {msg}"
        self.alert_log.append(alert)
        print(alert)

    def operator_chat(self, msg):
        chat = f"[CHAT] {msg}"
        self.chat_log.append(chat)
        print(chat)

    def relay_ops_chat(self, msg):
        relay = f"[RELAY] {msg}"
        self.relay_stack.append(relay)
        print(relay)

    def mission_log_sync(self, data):
        json_sync = json.dumps(data, indent=2)
        log_msg = f"[LOGSYNC] {datetime.now().isoformat()}\n{json_sync}"
        self.sync_records.append(log_msg)
        print(log_msg)

    def ai_task_suggest(self, dump: list, context: str = "post-exploitation") -> None:
        print(f"[AI TASKING] Based on dump ({len(dump)} entries):")
        if "Administrator" in str(dump) or "krbtgt" in str(dump):
            print("👉 Suggest: Golden Ticket ops, lateral SMB, or domain pivot.")
        elif len(dump) == 0:
            print("🤖 Suggest: Retry credential extraction or escalate host access.")
        else:
            print("🧠 Recommend: Invoke Mimikatz pass-the-hash, explore AD structure.")

if __name__ == "__main__":
    com = ComLinkAI()
    com.send_to_hud("Agent connected.")
    com.send_alert("Test alert.")
    com.operator_chat("Mission started.")
    com.relay_ops_chat("Relay message.")
    com.mission_log_sync({"mission": "demo", "status": "active"})

    com.ai_task_suggest(["Administrator", "user1"], context="post-exploitation")
    com.ai_task_suggest(["Administrator", "user1"], context="post-exploitation")
    watchdog = AnomalyWatchdog()