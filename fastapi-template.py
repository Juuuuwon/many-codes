from fastapi import FastAPI, status


app = FastAPI()

@app.get("/")
def index():
    return {"message": "ok"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)    