import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criar a fila (caso ainda não exista)
channel.queue_declare(queue='minha_fila')

# Função que processa a mensagem
def callback(ch, method, properties, body):
    print(f" [x] Recebido {body}")

# Consumir mensagens da fila
channel.basic_consume(queue='minha_fila', on_message_callback=callback, auto_ack=True)
print(' [*] Aguardando mensagens. Para sair, pressione CTRL+C')
channel.start_consuming()
