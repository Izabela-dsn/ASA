from fastapi import FastAPI, HTTPException
from classes import Request_Aluno, Request_Professor, Request_Curso, Request_Curso_Aluno
from models import Aluno, session, Professor, Curso, CursoAluno
import logging 
from logging.config import dictConfig
import log_config
from send import send_payload
from receiver import receiver_send_db

app = FastAPI()
logger = logging.getLogger('foo-logger')


@app.get("/")
async def root():
    return {
        "status":"Success",
        "data": "no data"
    }

@app.get("/alunos")
async def get_all_alunos():
	try:
		logger.info("Starting query to get Alunos.")
		alunos_query = session.query(Aluno)
		alunos = alunos_query.all()
		if not alunos:
			raise HTTPException(status_code=404, detail="Aluno not found")
		return {
			"STATUS": "SUCCESS",
			"data": alunos
		}
	except Exception as e:
		logger.error(f"Is not possible to get Alunos: {str(e)}")
		raise HTTPException(status_code=500, detail="Failed to get Alunos")


@app.get("/professores")
async def get_all_professores():
	try:
		logger.info("Starting query to get Professores.")
		professores_query = session.query(Professor)
		professores = professores_query.all()
		if not professores:
			raise HTTPException(status_code=404, detail="Professores not found")
		return {
			"STATUS": "SUCCESS",
			"data": professores
		}
	except Exception as e:
		logger.error(f"Is not possible to get Professores: {str(e)}")
		raise HTTPException(status_code=500, detail="Failed to get Professores")


@app.get("/cursos")
async def get_all_cursos():
	try:
		logger.info("Starting query to get Cursos.")
		cursos_query = session.query(Curso)
		cursos = cursos_query.all()
		if not cursos:
			raise HTTPException(status_code=404, detail="Cursos not found")
		return {
			"STATUS": "SUCCESS",
			"data": cursos
		}
	except Exception as e:
		logger.error(f"Is not possible to get Cursos: {str(e)}")
		raise HTTPException(status_code=500, detail="Failed to get Cursos")


@app.get("/cursosAlunos")
async def get_all_cursosAlunos():
	try:
		logger.info("Starting query to get CursoAluno.")
		cursosAlunos_query = session.query(CursoAluno)
		cursosAlunos = cursosAlunos_query.all()
		if not cursosAlunos:
			raise HTTPException(status_code=404, detail="CursosAlunos not found")
		return {
			"STATUS": "SUCCESS",
			"data": cursosAlunos
		}
	except Exception as e:
		logger.error(f"Is not possible to get CursosAlunos: {str(e)}")
		raise HTTPException(status_code=500, detail="Failed to get CursosAlunos")



@app.post("/alunos")
async def criar_aluno(request_aluno: Request_Aluno):
	try:
		logger.info("Creating Aluno")
		aluno_json = request_aluno
		#print(aluno_json.nome)

		#aluno = Aluno(
		#	nome = aluno_json.nome,
		#	email = aluno_json.email,
		#	cpf = aluno_json.cpf,
		#	endereco = aluno_json.endereco
		#)

		aluno2 = {
			"nome" : aluno_json.nome,
			"email" : aluno_json.email,
			"cpf" : aluno_json.cpf,
			"endereco" : aluno_json.endereco
		}

		#session.add(aluno)
		#session.commit()
		send_payload(aluno2)
		print('oi')
		receiver_send_db()
		print('oi')
		
		return {
		"status": "SUCCESS",
		"data": aluno_json
		}
	except Exception as e:
		logger.error(f"Is not possible to create Alunos: {str(e)}")
		raise HTTPException(status_code=500, detail="Failed to create Alunos")



@app.post("/professores")
async def criar_professores(request_professor: Request_Professor):
	try:
		logger.info("Creating Professor")
		professor_json = request_professor

		professor = Professor(
			nome        = professor_json.nome,
			email       = professor_json.email,
			cpf         = professor_json.cpf,
			endereco    = professor_json.endereco,
			numero      = professor_json.numero,
			complemento = professor_json.complemento,
			cidade      = professor_json.cidade,
			estado      = professor_json.estado
		)
		session.add(professor)
		session.commit()

		return {
		"status": "SUCCESS",
		"data": professor_json
		}
	except Exception as e:
		logger.error(f"Is not possible to create Professor: {str(e)}")
		raise HTTPException(status_code=500, detail="Failed to create Professor")

@app.post("/cursos")
async def criar_cursos(request_curso: Request_Curso):
	try:
		logger.info("Creating Course")
		curso_json = request_curso

		curso = Curso(
			descricao = curso_json.descricao,
			professor_id = curso_json.professor_id
		)
		session.add(curso)
		session.commit()

		return {
		"status": "SUCCESS",
		"data": curso_json
		}
	except Exception as e:
		logger.error(f"Is not possible to create Curso: {str(e)}")
		raise HTTPException(status_code=500, detail="Failed to create Curso")

@app.post("/cursosAlunos")
async def post_aluno_in_curso(request_curso_aluno: Request_Curso_Aluno):
	try:
		logger.info("Adding Aluno in Curso")
		curso_aluno_json = request_curso_aluno

		request_curso_aluno = CursoAluno(
			idCurso = curso_aluno_json.idCurso,
			idAluno = curso_aluno_json.idAluno
		)
		session.add(request_curso_aluno)
		session.commit()

		return {
		"status": "SUCCESS",
		"data": request_curso_aluno
		}
	except Exception as e:
		logger.error(f"Is not possible to create CursoAluno: {str(e)}")
		raise HTTPException(status_code=500, detail="Failed to create CursoAluno")


@app.put("/alunos/{aluno_id}")
async def alterar_aluno(aluno_id: int, request_aluno: Request_Aluno):
	try:
		aluno_json = request_aluno
		aluno_query = session.query(Aluno).filter(
			Aluno.id == aluno_json.id
		)
		aluno = aluno_query.first()
		if not aluno:
			raise HTTPException(status_code=404, detail="Aluno not found")
	
		aluno.nome = aluno_json.nome
		aluno.cpf = aluno_json.cpf
		aluno.email = aluno_json.email
		aluno.endereco = aluno_json.endereco

		session.add(aluno)
		session.commit()

		return {
			"status": "SUCESS",
			"data": aluno_json
		}
	except Exception as e:
		logger.error(f"Error upadating Aluno: {str(e)}")
		raise HTTPException(status_code=500, detail="Error upadating Aluno")

@app.put("/professores/{professor_id}")
async def alterar_professor(professor_id: int, request_professor: Request_Professor):
	try:
		professor_json = request_professor
		professor_query = session.query(Professor).filter(
			Professor.id == professor_json.id
		)
		professor = professor_query.first()
		if not professor:
			raise HTTPException(status_code=404, detail="Professor not found")
	
		professor.nome        = professor_json.nome,
		professor.email       = professor_json.email,
		professor.cpf         = professor_json.cpf,
		professor.endereco    = professor_json.endereco,
		professor.numero      = professor_json.numero,
		professor.complemento = professor_json.complemento,
		professor.cidade      = professor_json.cidade,
		professor.estado      = professor_json.estado

		session.add(professor)
		session.commit()

		return {
			"status": "SUCESS",
			"data": professor_json
		}
	except Exception as e:
		logger.error(f"Error upadating professor: {str(e)}")
		raise HTTPException(status_code=500, detail="Error upadating professor")

@app.put("/cursos/{cursos_id}")
async def alterar_curso(cursos_id: int, request_curso: Request_Curso):
	try:
		curso_json = request_curso
		curso_query = session.query(Curso).filter(
			Curso.id == curso_json.id
		)
		curso = curso_query.first()
		if not curso:
			raise HTTPException(status_code=404, detail="curso not found")
	
		curso.descricao        = curso_json.descricao,
		curso.professor_id       = curso_json.professor_id

		session.add(curso)
		session.commit()

		return {
			"status": "SUCESS",
			"data": curso_json
		}
	except Exception as e:
		logger.error(f"Error upadating curso: {str(e)}")
		raise HTTPException(status_code=500, detail="Error upadating curso")

