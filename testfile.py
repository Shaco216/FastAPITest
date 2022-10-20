from fastapi import FastAPI

app = FastAPI()

dict = {
    "name": "Test",
    "number": 1
}

dict_dict = {
    "1": {
      "name": "Test1",
      "number": 1
    },
    "2": {
      "name": "Test2",
      "number": 2
    }
}

a = dict_dict["1"]
print(a)

@app.get("/dict")
async def root():
    return dict

@app.get("/dict-dict")
async def root():
    return dict_dict

@app.get("/item/{item_id}")
async def item(item_id):
    return {dict_dict[item_id]}