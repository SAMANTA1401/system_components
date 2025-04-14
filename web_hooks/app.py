from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/webhook")
async def webhook_listener(request: Request):
    payload = await request.json()
    print("📦 Webhook received:", payload)
    return {"message": "Webhook received successfully!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
