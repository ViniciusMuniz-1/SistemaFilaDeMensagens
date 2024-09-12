from flask import Flask, request
import pika

app = Flask(__name__)

def enviar_mensagem(mensagem):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.basic_publish(exchange='', routing_key='minha_fila', body=mensagem)
    connection.close()

@app.route('/enviar', methods=['POST'])
def enviar():
    dados = request.get_json()
    mensagem = dados.get('mensagem', 'Mensagem padrão')
    enviar_mensagem(mensagem)
    return "Mensagem enviada com sucesso", 200

if __name__ == '__main__':
    app.run(debug=True)
