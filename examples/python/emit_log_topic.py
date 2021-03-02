#!/usr/bin/env python
import pika
import sys
import json

rabbitmq_username = 'admin'
rabbitmq_password = 'ccis2010'
rabbitmq_ip = 'localhost'
rabbitmq_port = '5672'
rabbitmq_vhost = '/'
exchange='psu'

credentials = pika.PlainCredentials(rabbitmq_username, rabbitmq_password)
				
connection_parameters = pika.ConnectionParameters(rabbitmq_ip, rabbitmq_port, rabbitmq_vhost, credentials)
connection = pika.BlockingConnection(
    connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic', durable=True)

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
json_to_send = json.dumps({'message': message})

channel.basic_publish(
    exchange=exchange, routing_key=routing_key, body=json_to_send)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()