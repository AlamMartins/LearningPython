from menu import menu
from api import app
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get('/get-item/{item_id}')
def get_item(
    item_id: int = Path(
        None,
        description="Fill with ID of the item you want to view")):

    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search == []:
        return {'Error': 'Item does not exist'}

    return {'Item': search[0]}


@app.get('/get-by-name')
def get_item(name: str = None):
# def get_item(name: Optional[str] = None):

    search = list(filter(lambda x: x.get("name") == name, menu))
    search = list(filter(lambda x: x["name"] == name, menu))

    if search == []:
        return {'item': 'Does not exist'}

    return {'Item': search[0]}
  

