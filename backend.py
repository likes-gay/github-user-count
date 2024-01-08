from fastapi import FastAPI, WebSocket
import time

app = FastAPI()

def user_count():
    #implement logic
    
    return(10, "John Doe", "https://avatars.githubusercontent.com/u/96008479") #placeholder values

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        user_count, last_user_name, last_user_pfp = user_count()
        await websocket.send_json({
            "user_count": user_count,
            "last_user_name": last_user_name,
            "last_user_pfp": last_user_pfp,
            "time": time.time()    
        })