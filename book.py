from fastapi import FastAPI 
import json
app = FastAPI()

def load_data():
    with open("books.json",'r') as f:
        data = json.load(f)
        return data

@app.get('/')
def welcome():
    return {"message":"Hey there, Welcome to my Library API"}

@app.get('/about')
def info():
    return {"message":"This api purpose is to give info about books with their author,title and rating"}

@app.get('/books')
def book_info():
    data = load_data()
    return data