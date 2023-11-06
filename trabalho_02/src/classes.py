from pydantic import BaseModel

class Request_Aluno(BaseModel):
	id: int
	nome: str
	email: str
	cpf: str
	endereco: str

class Request_Professor(BaseModel):
    id: int
    nome: str
    email: str
    cpf: str
    endereco: str
    numero: str
    complemento: str
    cidade: str
    estado: str

class Request_Curso(BaseModel):
    id: int
    descricao: str
    professor_id: int

class Request_Curso_Aluno(BaseModel):
    id: int
    idCurso: int
    idAluno: int