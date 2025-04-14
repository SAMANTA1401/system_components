from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

# Store connected clients
clients = []


html = """
<!DOCTYPE html>
<html>
<head>
    <title>FastAPI WebSocket Chat</title>
</head>
<body>
    <h2>FastAPI WebSocket Chat</h2>
    <ul id="messages"></ul>
    <input id="msgInput" autocomplete="off"/><button onclick="sendMessage()">Send</button>

    <script>
        const ws = new WebSocket("ws://localhost:8000/ws");

        ws.onmessage = function(event) {
            const messages = document.getElementById('messages');
            const message = document.createElement('li');
            message.innerText = event.data;
            messages.appendChild(message);
        };

        function sendMessage() {
            const input = document.getElementById("msgInput");
            ws.send(input.value);
            input.value = '';
        }
    </script>
</body>
</html>
"""
# WebSockets solve this problem by allowing continuous, two-way communication
# between the client and server over a single persistent connection.

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in clients:
                await client.send_text(f"Message: {data}")
    except WebSocketDisconnect:
        clients.remove(websocket)
