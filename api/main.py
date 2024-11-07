from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders, sandwiches, resources, recipes, order_details
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)

@app.post("/sandwiches/", response_model=schemas.Order, tags=["sandwiches"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db=db, order=order)


@app.get("/sandwiches/", response_model=list[schemas.Order], tags=["sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)


@app.get("/sandwiches/{order_id}", response_model=schemas.Order, tags=["sandwiches"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = sandwiches.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/sandwiches/{order_id}", response_model=schemas.Order, tags=["sandwiches"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = sandwiches.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwiches.update(db=db, order=order, order_id=order_id)


@app.delete("/sandwiches/{order_id}", tags=["sandwiches"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = sandwiches.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwiches.delete(db=db, order_id=order_id)

# Create
@app.post("/resources/", response_model=schemas.Order, tags=["resources"])
def create_resource(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, order=order)

# Read All
@app.get("/resources/", response_model=list[schemas.Order], tags=["resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)

# Read One
@app.get("/resources/{order_id}", response_model=schemas.Order, tags=["resources"])
def read_one_resource(order_id: int, db: Session = Depends(get_db)):
    order = resources.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return order

# Update
@app.put("/resources/{order_id}", response_model=schemas.Order, tags=["resources"])
def update_resource(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = resources.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.update(db=db, order=order, order_id=order_id)

# Delete
@app.delete("/resources/{order_id}", tags=["resources"])
def delete_resource(order_id: int, db: Session = Depends(get_db)):
    order = resources.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.delete(db=db, order_id=order_id)

# Create
@app.post("/recipes/", response_model=schemas.Order, tags=["recipes"])
def create_recipe(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, order=order)

# Read All
@app.get("/recipes/", response_model=list[schemas.Order], tags=["recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)

# Read One
@app.get("/recipes/{order_id}", response_model=schemas.Order, tags=["recipes"])
def read_one_recipe(order_id: int, db: Session = Depends(get_db)):
    order = recipes.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return order

# Update
@app.put("/recipes/{order_id}", response_model=schemas.Order, tags=["recipes"])
def update_recipe(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = recipes.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes.update(db=db, order=order, order_id=order_id)

# Delete
@app.delete("/recipes/{order_id}", tags=["recipes"])
def delete_recipe(order_id: int, db: Session = Depends(get_db)):
    order = recipes.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes.delete(db=db, order_id=order_id)

# Create
@app.post("/order_details/", response_model=schemas.Order, tags=["order_details"])
def create_order_detail(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return order_details.create(db=db, order=order)

# Read All
@app.get("/order_details/", response_model=list[schemas.Order], tags=["order_details"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)

# Read One
@app.get("/order_details/{order_id}", response_model=schemas.Order, tags=["order_details"])
def read_one_order_detail(order_id: int, db: Session = Depends(get_db)):
    order = order_details.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return order

# Update
@app.put("/order_details/{order_id}", response_model=schemas.Order, tags=["order_details"])
def update_order_detail(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = order_details.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return order_details.update(db=db, order=order, order_id=order_id)

# Delete
@app.delete("/order_details/{order_id}", tags=["order_details"])
def delete_order_detail(order_id: int, db: Session = Depends(get_db)):
    order = order_details.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return order_details.delete(db=db, order_id=order_id)
