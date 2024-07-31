from menu import menu # Base de Dados "Menu"
from fastapi import FastAPI, Path, HTTPException, Query #fastapi é um framework para APIs.


app = FastAPI() #criando uma instância do FASTAPI


""
"----------------- ROTAS API  -----------------"
""


@app.get("/get-item/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"),
    q: str | None = Query(default=None, alias="item-query"),
):
    search = list(filter(lambda x: x["id"] == item_id, menu ))

    if not search:
        raise HTTPException(status_code=404, detail="Falha na busca, não foi encontrado o item referente a esse id.")
    # if q:
        # results.update({"q": q})
    return search


# #Function get_item (Captura o valor conforme o ID informado no parâmetro)
# @app.get('/get-item/{item_id}')
# def get_item(item_id: int = Path(..., description="Fill with ID of the item you want to view")):

#     search = list(filter(lambda x: x["id"] == item_id, menu))

#     if not search:
#         raise HTTPException(status_code=404, detail="Item does not exist")

#     return {'Item': search[0]}


#Function get_item (Captura o valor conforme o ID informado no parâmetro)
@app.get("/")
def hello_world_root():
    return {"Logger": "Hello World"}


""
"----------------- ROTAS API  -----------------"
""



# class Item(BaseModel):
#     name: str = None
#     price: float


# class UpdateItem(BaseModel):
#     name: str = None
#     price:  None

# @app.get('/get-item/{item_id}')
# def get_item(
#     item_id: int = Path(
#         None,
#         description="Fill with ID of the item you want to view")):

#     search = list(filter(lambda x: x["id"] == item_id, menu))

#     if search == []:
#         return {'Error': 'Item does not exist'}

#     return {'Item': search[0]}


# @app.get('/get-by-name')
# def get_item(name: str = None):
# # def get_item(name: Optional[str] = None):

#     search = list(filter(lambda x: x["name"] == name, menu))

#     if search == []:
#         return {'item': 'Does not exist'}

#     return {'Item': search[0]}
#     return {'Item': search[0]}


# @app.get('/list-menu')
# def list_menu():
#     return {'Menu': menu}


# @app.post('/create-item/{item_id}')
# def create_item(item_id: int, item: Item):

#     search = list(filter(lambda x: x["id"] == item_id, menu))

#     if search != []:
#         return {'Error': 'Item exists'}

#     item = item.dict()
#     item['id'] = item_id

#     menu.append(item)
#     return item


# @app.put('/update-item/{item_id}')
# def update_item(item_id: int, item: UpdateItem):

#     search = list(filter(lambda x: x["id"] == item_id, menu))

#     if search == []:
#         return {'Item': 'Does not exist'}

#     if item.name is not None:
#         search[0]['name'] = item.name

#     if item.price is not None:
#         search[0]['price'] = item.price

#     return search


# @app.delete('/delete-item/{item_id}')
# def delete_item(item_id: int):
#     search = list(filter(lambda x: x["id"] == item_id, menu))

#     if search == []:
#         return {'Item': 'Does not exist'}

#     for i in range(len(menu)):
#         if menu[i]['id'] == item_id:
#             del menu[i]
#             break
#     return {'Message': 'Item deleted successfully'}