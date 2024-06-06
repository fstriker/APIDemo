from fastapi import FastAPI
import random
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/register")
def register_device():
    return {f"Registration was successful, ID: {random.randrange(0,50000)}"}

if __name__ == '__main__':
    uvicorn.run(app, port=80, host='0.0.0.0')
