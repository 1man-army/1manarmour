from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import threading

app = Flask(__name__)
socketio = SocketIO(app)

agents = {}  # agent_id: {status, logs, cpu, ram, ...}

@app.route("/")
def dashboard():
    return render_template("dashboard.html", agents=agents)

@app.route("/api/voice", methods=["POST"])
def voice_command():
    cmd = request.json.get("cmd")
    agent_id = request.json.get("agent_id")
    # Relay command to agent (stub)
    # emit to agent via socketio or other comms
    return jsonify({"status": "sent", "cmd": cmd, "agent_id": agent_id})

@socketio.on("connect")
def handle_connect():
    emit("init", agents)

def update_agent(agent_id, data):
    agents[agent_id] = data
    socketio.emit("agent_update", {agent_id: data})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)