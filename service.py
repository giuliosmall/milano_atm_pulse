from datetime import datetime

def get_service():
    return {
        "status": "Up & running",
        "now": datetime.now(),
        "routes": ["/traffic", "/status", "/news"]
    }
