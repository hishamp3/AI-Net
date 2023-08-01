from fastapi import FastAPI, Request
from .aggregation import edgeNodeConsumer
from .ports import edgeNode1
from .dtree import decisionTree

app = FastAPI()
model = decisionTree()


@app.get("/")
async def root():
    return {"message": "Hello World", "new": "message"}


@app.get("/get_params")
async def update_hyperparams():
    try:
        return model.hyperparameters
    except:
        return {"status": "failed to get"}


@app.post("/set_params")
async def update_hyperparams(request_data: Request):
    data = await request_data.json()
    if type(data) is dict and data != {}:
        model.hyperparameters = data
