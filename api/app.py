from http import HTTPStatus
from fastapi import FastAPI, HTTPException
from typing import List

from models import Blog, BlogType, BlogVisibility
from serializers import BlogSerializer

app = FastAPI()


@app.get('/blogs/', response_model=List[Blog])
async def get_blogs():
    serializer = BlogSerializer()
    return serializer.get_instances()


@app.get('/blogs/{item_id}', response_model=Blog)
async def get_blog(item_id: int):
    try:
        serializer = BlogSerializer()
        return serializer.get_instance(item_id)
    except:
        raise HTTPException(status_code=400, detail='Detail not found')


@app.post('/blogs/', response_model=Blog, status_code=201)
async def create_blog(blog: Blog):
    try:
        serializer = BlogSerializer()
        return serializer.create_instance(blog)
    except BaseException as e:
        raise e or HTTPException(status_code=500)

@app.put('/blogs/{item_id}')
async def update_blog(blog: Blog, item_id: int):
    try:
        serializer = BlogSerializer()
        serializer.update_instance(item_id, blog)
    except:
        raise HTTPException(status_code=500)

@app.delete('/blogs/{item_id}')
async def delete_blog(item_id: int):
    try:
        serializer = BlogSerializer()
        serializer.delete_instance(item_id)
    except:
        raise HTTPException(status_code=500)
