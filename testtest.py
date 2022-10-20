from fastapi import FastAPI

app = FastAPI()

dict = {
    "name": "Test",
    "number": 1
}

dict_dict = {
    1: {
      "name": "Test1",
      "number": 1
    },
    2: {
      "name": "Test2",
      "number": 2
    }
}

@app.get("/dict")
async def getDict():
    return dict

@app.get("/dict-dict")
async def getDictDict():
    return dict_dict

@app.get("/dict-index/{dict_index}")
async def getDictAtIndex(dict_index):
    return dict_dict[int(dict_index)]