from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name" : "Monitor"},
    {"item_name" : "Teclado"},
    {"item_name" : "Mouse"},
]

# http://127.0.0.1:8000/items/?skip=0&limit=10
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

## Parámetro opacionales
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id" : item_id, "q" : q}
    return {"item_id" : item_id}


# Multiples parametros de path y de query
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int,
        item_id: str,
        q: str | None = None,
        short: bool = False,
):
    #1) Armo la respuesta base
    item = {"item_id": item_id, "owner_id": user_id}
    # 2) Si enviaron q,lo agrego
    if q:
        item["q"] = q
    # 3) Si short es False, agrego una descripcion larga
    if not short:
        item["decripcion"] = "Descripcion larga del item"
    # 4) Devuelvo el JSON final
    return item

@app.get("/items1/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item