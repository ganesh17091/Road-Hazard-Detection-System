# driver_display.py
import socket, json, time

PORT = 5005

def level(size):
    if size < 20000: return "FAR"
    if size < 60000: return "NEAR"
    return "DANGER"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", PORT))

print("Driver Display Active\n")

while True:
    data, addr = sock.recvfrom(65535)
    msg = json.loads(data.decode())
    if not msg["objects"]: continue

    best = max(msg["objects"], key=lambda o: o["size"])
    status = level(best["size"])

    if status == "DANGER":
        alert = f"🚨 DANGER: {best['object_type'].upper()} VERY CLOSE – SLOW DOWN!"
    elif status == "NEAR":
        alert = f"⚠ WARNING: {best['object_type'].upper()} NEAR AHEAD"
    else:
        alert = f"ℹ FAR OBJECT AHEAD"

    print(f"[{time.strftime('%H:%M:%S')}] {alert}")
