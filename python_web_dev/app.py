from fastapi import FastAPI, UploadFile
import uvicorn

app = FastAPI()

@app.get('/')
def home():
    return {'data': 'welcome to home page'}

@app.get('/contact')
def contact():
    return {'data': 'welcome to contact page'}

@app.post('/upload')
def handleImage(files: list[UploadFile]):
    print(files)
    return {'status': 'got the files'}

uvicorn.run(app)
