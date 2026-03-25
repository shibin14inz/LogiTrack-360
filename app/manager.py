from fastapi import WebSocket
from typing import Dict, List

class ConnectionManager:
    def __init__(self):
        self.active_trucks: Dict[int, WebSocket] = {}
        self.admin_connections: List[WebSocket] = []

    async def connect_truck(self, truck_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_trucks[truck_id] = websocket

    async def connect_admin(self, websocket: WebSocket):
        await websocket.accept()
        self.admin_connections.append(websocket)

    async def broadcast_to_admins(self, message: dict):
        for connection in self.admin_connections:
            await connection.send_json(message)

    def disconnect_truck(self, truck_id: int):
        if truck_id in self.active_trucks:
            del self.active_trucks[truck_id]

manager = ConnectionManager()