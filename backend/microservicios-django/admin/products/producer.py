import json

import pika

# from django.conf import settings

# MY_AMPQS = settings.MY_AMPQS
params = pika.URLParameters('amqps://iuwnhvov:e86m8BldW8Deo5FWsb-FJU-jYf1_N21d@eagle.rmq.cloudamqp.com/iuwnhvov')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
