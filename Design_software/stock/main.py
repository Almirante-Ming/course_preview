from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from stock.schemas import Product
from uuid import uuid4

stock = FastAPI()

pdt_list={}

@stock.get('/')
def read_products():
    return pdt_list

@stock.post('/new_pdt/', response_model=Product, status_code=HTTPStatus.CREATED)
def stock_pdt(product: Product):
    prod_id= str(uuid4())
    if prod_id in pdt_list:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Already exists")

    else:
        pdt_list[prod_id] = product
        return product