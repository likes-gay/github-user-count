from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
import time

app = FastAPI()

def user_count():
    #implement logic
    
    return(10, "John Doe", "https://avatars.githubusercontent.com/u/96008479") #placeholder values


@app.get("/sse")
async def message_stream(request: Request):
    async def event_generator():
        while True:
            if await request.is_disconnected():
                break

            count, last_user_name, last_user_pfp = user_count()
            yield {
                "event": "message",
                "data": {
                    "user_count": count,
                    "last_user_name": last_user_name,
                    "last_user_pfp": last_user_pfp,
                    "time": time.time()    
                }
            }

            time.sleep(1)

    return EventSourceResponse(event_generator())
