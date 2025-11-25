# v2v_sender.py
import cv2, json, time, socket
from ultralytics import YOLO
import gpsd

VEHICLE_ID = "CAR_01"
MODEL = "yolo11n.pt"
PORT = 5005
BCAST = "255.255.255.255"

gpsd.connect()
model = YOLO(MODEL)
cam = cv2.VideoCapture(0)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    ret, frame = cam.read()
    if not ret: continue
    results = model(frame, verbose=False)[0]
    
    objs = []
    for box in results.boxes:
        x1,y1,x2,y2 = box.xyxy[0].tolist()
        objs.append({
            "object_type": results.names[int(box.cls[0])],
            "size": round((x2-x1)*(y2-y1),2)
        })

    lat, lon = gpsd.get_current().position()
    
    payload = {
        "vehicle_id": VEHICLE_ID,
        "timestamp": time.time(),
        "gps": {"lat": lat, "lon": lon},
        "num_detections": len(objs),
        "objects": objs
    }

    sock.sendto(json.dumps(payload).encode(), (BCAST, PORT))
