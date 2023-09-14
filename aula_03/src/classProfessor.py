from pydantic import BaseModel

class Request_Professor(BaseModel):
    id = int
    nome        = str
    email       = str
    cpf         = str
    endereco    = str
    numero      = str
    complemento = str
    cidade      = str
    estado      = str

