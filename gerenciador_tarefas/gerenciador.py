from fastapi import FastAPI

app = FastAPI()

TAREFAS = ["1"]


@app.get("/tarefas")
def listar():
    return TAREFAS
