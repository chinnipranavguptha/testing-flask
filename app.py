from flask import Flask
import os
import datetime
import pytz
import subprocess
import psutil

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Chinni pranav guptha"  # Replace with your full name
    username = os.getenv("USER", os.getenv("USERNAME", "Pranav"))

    # Get server time in IST
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

    # Get top output
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000)