import uvicorn
from fastapi import FastAPI,WebSocket
from starlette.responses import FileResponse 
from typing import List

app = FastAPI()
connections: List[WebSocket] = []

@app.get("/")
async def read_root():
    return FileResponse('index.html')

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            print(f"User: {message}")
            
            response = f"Bot: You said '{message}'"
            await websocket.send_text(response)
            
            # Broadcast to all connected clients (optional)
            for conn in connections:
                if conn != websocket:
                    await conn.send_text(f"New message: {message}")
    except:
        connections.remove(websocket)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)