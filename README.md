# ASA

Para rodar as aulas no windows:

1. Crie um ambiente virtual <br />
<code>pip install virtualenv
 virtualenv nome_da_virtualenv</code>

2. Ative o ambiente <br/>
<code> venv/Scripts/activate </code>

3. Instale o FastAPI <br/>
<code> pip install fastapi
 pip install uvicorn</code>

5. Rode o programa dentro da pasta <strong>src</strong> <br/>
<code>uvicorn main:app --reload</code>
