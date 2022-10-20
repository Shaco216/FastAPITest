from fastapi import *
import json

from pydantic import BaseModel
# start per terminal mit:
# uvicorn main:app --reload

# https://fastapi.tiangolo.com/tutorial/first-steps/

# Session kann per ctrl+c beendet werden
app = FastAPI()

# Dict to Json
itemspecs = {
    1: {
        "name": "Brett",
        "laenge": 4
        },
    2: {
        "name": "Stein",
        "laenge": 3
    }
}
itemtestspecs = [{"name": "Brett", "laenge": 4},{"name": "Stein", "laenge": 3}]
testdict = {"test": "Brett", "breite": 4}
json_objecttest = json.dumps(testdict)
loaded_obj_test = json.loads(json_objecttest)
print(json_objecttest)

print(json.dumps(itemspecs[1]) is str)
print(type(json.dumps(itemspecs[1])))

class Thing(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
#geht kann nicht per browser getestet werden oder über /docs

@app.post("/things/")
async def create_item(thing: Thing):
    return thing

@app.get("/")
async def read_root():
    return {"API Präsentation"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return itemspecs[int(item_id)]

    #json_object = json.dumps(itemtestspecs[item_id])
    #loaded_obj_test = json.loads(json_object)
    #return {loaded_obj_test}

    #json_object = json.dumps(itemspecs[item_id])
    #loaded_obj_test = json.loads(json_object)
    #return {"Beispiel für einen Internal Server Error" : loaded_obj_test}#itemspecs[item_id]
    #return {"test": json_object}
    #return {loaded_obj_test['breite']}#nur ein key: breite

@app.get("/json")
async def json():
    print(json_objecttest)
    print("ich bin: " +str(type(json_objecttest)))
    return {json_objecttest}

@app.get("/Ende")
async def end_praes():
    return {"Gibts noch Fragen?"}


@app.get("/ende")
async def end_praes():
    return {"Gibts noch Fragen?"}

