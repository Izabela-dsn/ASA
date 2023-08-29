from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import logging
from logging.config import dictConfig
from config import log_config

dictConfig(log_config)


app = FastAPI()
logger = logging.getLogger('foo-logger')


class Aluno(BaseModel):
    nome: str
    matricula: str
    curso: str
    faculdade: str

class UpdateAluno(BaseModel):
    nome: str = None
    matricula: str = None
    curso: str = None
    faculdade: str = None

dados_alunos = [
    {
        'nome':'Diana do Nascimento',
        'matricula': '12356EGF98',
        'curso': 'Engenharia Florestal',
        'faculdade': 'Faculdade de Engenharia'
    }
]


@app.get("/alunos")
async def mostrar_alunos ():
    try:
        logger.info("Mostrando estudantes")
        return dados_alunos
    except:
        logger.error('Não foi possivel mostrar os estudantes.')


@app.post("/alunos/criar")
async def criar_alunos(aluno: Aluno):
    try:
        aluno = aluno.dict()
        dados_alunos.append(aluno)
        logger.info("Aluno registrado.")
        return aluno
    except:
        logger.error("Not possible post now")
        return {"response":"Não foi possivel adicionar um aluno, tente novamente mais tarde."}
    

@app.put("/alunos/editar/{matricula}", response_model = Aluno)
async def editar_aluno(matricula:str, aluno:UpdateAluno):
    try:
        busca = list(filter(lambda estudante: estudante["matricula"] == matricula, dados_alunos))

        if busca == []:
            logger.error("Matricula não encontrada")
            return {'Matricula não encontrada!'}

        if aluno.nome is not None:
            busca[0]['nome'] = aluno.nome

        if aluno.matricula is not None:
            busca[0]['matricula'] = aluno.matricula

        if aluno.curso is not None:
            busca[0]['curso'] = aluno.curso

        if aluno.faculdade is not None:
            busca[0]['faculdade'] = aluno.faculdade

        logger.info("Aluno atualizado com sucesso!")
        return busca
    except:
        logger.error("Não foi possivel atualizar")

    

@app.delete("/alunos/apagar/{matricula}")
async def apagar_aluno(matricula:str):
    try:
        busca = list(filter(lambda estudante: estudante["matricula"] == matricula, dados_alunos))

        if busca == []:
            logger.error("Matricula não encontrada")
            return {'Matricula não encontrada!'}

        for i in range(len(dados_alunos)):
            if dados_alunos[i]['matricula'] == matricula:
                del dados_alunos[i]
                break

        logger.info("Aluno deletado com sucesso!")
        return {"Message" : 'Aluno deletado com sucesso!'}
    except:
        logger.error("Não foi possivel deletar o aluno")
        return {"Message" : 'Não foi possivel deletar o aluno'}