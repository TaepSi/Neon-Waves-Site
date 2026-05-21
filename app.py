from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

DB = messages.db

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute(
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    )
    conn.commit()
    conn.close()

@app.route()
def home()
    return jsonify({status ok})

@app.route(send-message, methods=[POST])
def send_message()
    data = request.get_json()
    name = data.get(name, ).strip()
    email = data.get(email, ).strip()
    message = data.get(message, ).strip()
    if not name or not email or not message
        return jsonify({error All fields required}), 400
    conn = sqlite3.connect(DB)
    conn.execute(
        INSERT INTO messages (name, email, message, created_at) VALUES (, , , ),
        (name, email, message, datetime.now().strftime(%Y-%m-%d %H%M))
    )
    conn.commit()
    conn.close()
    return jsonify({success True})

@app.route(messages)
def list_messages()
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(SELECT  FROM messages ORDER BY created_at DESC).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

if __name__ == __main__
    import os
    init_db()
    port = int(os.getenv(PORT, 10000))
    app.run(host=0.0.0.0, port=port)
