"""
Main Dashboard - Professor&Master Memorable
Operator dashboard entry point: live agent view, notes, mode switch, and voice command integration.
"""
import sys
from cp_opereatorex.tools.note_console import show_notes
from cp_opereatorex.tools.mode_switch import switch_mode
from cp_opereatorex.tools.voice_router import route_voice_command
from cp_opereatorex.comms.comlink_ai import ComLinkAI
from core.opsec.anomaly_watchdog import AnomalyWatchdog
from core.ai.ai_task_suggest import suggest_tasks
from core.lateral.pass_the_hash import automate_lateral_movement
from core.lateral.kerberos_probe import extract_kerberos_tickets

def show_dashboard():
    while True:
        print("\n=== Professor&Master Operator Dashboard ===")
        print("1. View Agents")
        print("2. View Notes")
        print("3. Switch Mode")
        print("4. Voice Command")
        print("5. Exit")
        choice = input("Select option: ").strip()
        if choice == "1":
            print("[AGENTS] (Stub) List of connected agents would appear here.")
        elif choice == "2":
            show_notes()
        elif choice == "3":
            mode = input("Enter mode (red/blue/stealth): ").strip()
            switch_mode(mode)
        elif choice == "4":
            cmd = input("Speak or type command: ").strip()
            route_voice_command(cmd)
        elif choice == "5":
            print("Exiting dashboard.")
            sys.exit(0)
        else:
            print("Invalid option.")

if __name__ == "__main__":
    show_dashboard()