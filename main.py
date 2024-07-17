from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI() 

@app.get('/')
def index():
    return {'data' : 'blog list'} 

@app.get('/blog')
def index(limit=10,published:bool = True, sort: Optional[str] = None):
    if published:
        return {'data' : f'{limit} published blogs from the db .'} 
    else:
        return {'data' : f'{limit} blogs from the db .'} 

@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'all unpublished blogs'} 

@app.get('/blog/{id}')
def show(id:int):
    return {'data' : id} 

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data' : {'1','2'} } 



class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data' : f'Blog is created with title as {blog.title}'}


# To change the port use the below lines and run the command python main.py
# if __name__ == "__main__" :
#     uvicorn.run(app, host="127.0.0.1", port=9000)