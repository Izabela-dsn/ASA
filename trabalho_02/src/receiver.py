import pika, json
from models import session, Aluno
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

def receiver_send_db():
    try:
        url = URL.create(
            drivername='postgresql+psycopg2',
            username='postgres',
            password='banco',
            host='localhost',
            database='postgres',
            port=5432
        )

        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        session = Session()

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        # channel.queue_declare(queue='aluno')

        print("Consumer started...")

        def callback(ch, method, properties, body):
            print('Received message:')
            dados_mensagem = json.loads(body.decode())
            print(dados_mensagem)

            novo_aluno = Aluno(
                nome=dados_mensagem.get('nome'),
                email=dados_mensagem.get('email'),
                cpf=dados_mensagem.get('cpf'),
                endereco=dados_mensagem.get('endereco')
            )
            session.add(novo_aluno)
            session.commit()

            connection.close()


        while True:
            method_frame, header_frame, body = channel.basic_get(queue='aluno',auto_ack=True)

            if method_frame:
                callback(None, method_frame, None, body)
                break

        #usado para escuta continua
        #channel.basic_consume(queue='aluno', on_message_callback=callback, auto_ack=True)
        #channel.start_consuming()
        

    except Exception as e:
        print(f"Error: {e}")


