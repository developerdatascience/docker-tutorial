from fastapi import FastAPI



app = FastAPI() 

@app.get("/")
async def read_home():
    return "Welome to the FastAPI Dockerized Application!"

@app.get("/contact")
async def read_contact():
    return "Contact us at: support@example.com"
