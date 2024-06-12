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

@app.get("/fl-runs/{")
def register_device():
    return {f"Collection of FL runs"}

@app.get("/fl-runs/{runid}/participants")
def register_device():
    return {f"The participants with the following IDs are participating: {random.randrange(0,50000)},{random.randrange(0,50000)},{random.randrange(0,50000)},{random.randrange(0,50000)}"}

@app.get("/fl-runs/{runid}/configuration")
def get_fl_run_configuration():
    return {f"FL run configuration: {'learning_rate:10', 'fl_rounds:100'}"}

@app.get("/fl-runs/{runid}/global-model")
def get_fl_run_global_model():
    return {f"Global model: {[0.32,1.02,123.04,0.230]}"}

@app.get("/fl-runs/{runid}/client-models")
def post_fl_run_client_models():
    return {f"POST client model"}

@app.get("/fl-runs/{runid}/evaluation-results")
def post_fl_run_evaluation_results():
    return {f"POST evaluation results"}

@app.get("/fl-runs/{runid}/status")
def get_fl_run_status():
    return {f"FL run finished"}








if __name__ == '__main__':
    uvicorn.run(app, port=80, host='0.0.0.0')
