# Sistema de Mensagens com RabbitMQ e API Gateway

Este projeto é uma implementação de um sistema de filas de mensagens usando o **RabbitMQ** como Message-Oriented Middleware (MOM), com processos publicadores e consumidores. Um API Gateway foi criado para enviar mensagens para o RabbitMQ, e consumidores processam essas mensagens.

## Estrutura do Projeto

- **Publicador (Produtor)**: Envia mensagens para uma fila no RabbitMQ por meio de uma API.
- **Consumidor (Assinante)**: Consome e processa as mensagens da fila.
- **RabbitMQ**: Middleware que gerencia a fila de mensagens.

## Tecnologias Utilizadas

- **Python**
- **Flask** (para o API Gateway)
- **RabbitMQ** (para filas de mensagens)
- **Pika** (biblioteca Python para interação com RabbitMQ)

## Requisitos

- **Python 3.6+**
- **Docker** (para rodar o RabbitMQ) ou RabbitMQ instalado localmente.
- **Bibliotecas Python**:
  - `pika`
  - `flask`

## Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
### 2. Instalar Dependências
```
pip install -r requirements.txt
```

### 3. Executar o RabbitMQ
```
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```

Isso iniciará o RabbitMQ e a interface de administração estará disponível em http://localhost:15672. As credenciais padrão são:

Usuário: guest
Senha: guest

### 4. Rodar o Consumidor
Este processo consumirá as mensagens da fila.
```
python consumidor.py
```

### 5. Rodar o API Gateway
```
python api_gateway.py
```

### 6. Enviar Mensagens para o RabbitMQ
```
curl -X POST http://localhost:5000/enviar -H "Content-Type: application/json" -d '{"mensagem": "Hello, World!"}'
```