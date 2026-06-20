from browser_use import Agent, Browser
import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Agent running"}

@app.post("/run")
def run_agent(task: str):
    browser = Browser()
    agent = Agent(task=task, browser=browser)
    result = agent.run()
    return {"result": str(result)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
