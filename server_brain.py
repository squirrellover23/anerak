import uvicorn
from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import json
from Users import user
import Images
from Profile import profile, login
app = FastAPI()
with open("htmldirectory/home.html", 'r') as f:
    html = f.read()

# draw = ['rect', [[x, y, width, height], [color ], 0]]


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        print('connected')
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket, type: str = 'string'):
        if type == 'json':
            await websocket.send_json(message)
        else:
            await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


class connections:
    def __init__(self, websocket, client_id, man: ConnectionManager):
        self.man = man
        self.id = client_id
        self.websocket = websocket
        self.get_in = True
        self.send_draw = True
        self.user = user(self)

    def send_draw_info(self):
        return self.user.get_draw()

    def get_input(self, data):
        self.user.handle_input(data)


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    connect = connections(websocket, client_id, manager)

    try:
        info = json.dumps(Images.bianary_images)
        await websocket.send_json(info)
        for b in Images.bianary_data:
            await websocket.send_bytes(b)
            await websocket.receive_text()
        print(await websocket.receive_text())
        await manager.send_personal_message(connect.send_draw_info(), websocket)
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            connect.get_input(data)
            await manager.send_personal_message(connect.send_draw_info(), websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print('connection disconnected')


if __name__ == "__main__":
    uvicorn.run("server_brain:app", host="127.0.0.1", port=8001, log_level="info")
