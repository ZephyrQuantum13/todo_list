from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class TaskSchema(BaseModel):
    id: int
    title: str
    description: str | None = None

tasks: list[TaskSchema] = []



@app.get("/tasks")
def read_tasks() -> list[TaskSchema]:
    return tasks



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)