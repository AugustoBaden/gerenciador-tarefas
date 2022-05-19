from fastapi import FastAPI

app = FastAPI()

TAREFAS = [1,1,2]


@app.get("/tarefas")
def listar():
    return TAREFAS
