from fastapi import FastAPI


app = FastAPI()

@app.get("/tarefas")
def listar():
    return ""

TAREFAS = {}

@app.get("/tarefas")
def listar():
    return TAREFAS