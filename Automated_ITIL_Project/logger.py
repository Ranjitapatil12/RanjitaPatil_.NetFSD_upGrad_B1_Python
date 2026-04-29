import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "data", "logs.txt")


def log(message, level="INFO"):
    try:
        with open(LOG_FILE, "a") as file:
            file.write(f"{datetime.now()} [{level}] {message}\n")
    except Exception as e:
        print("Logging failed:", e)