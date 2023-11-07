import pika
import json

def send_payload(aluno):
    
    try:
    
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='aluno')

        #print(aluno)

        channel.basic_publish(exchange='',
                            routing_key='aluno',
                            body= json.dumps(aluno))
        
        print(json.dumps(aluno))

        connection.close()

        return 'success'
    except:
        return "failed"
