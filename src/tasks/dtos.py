from pydantic import BaseModel

class TaskSchemaDTO(BaseModel):
    title: str
    description: str
    is_completed: bool = False


class TaskResponseSchemaDTO(BaseModel):
    id :int
    title: str
    description: str
    is_completed: bool 