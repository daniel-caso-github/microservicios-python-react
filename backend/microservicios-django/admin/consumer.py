
import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Products

# from django.conf import settings

# MY_AMPQS = settings.MY_AMPQS
params = pika.URLParameters('amqps://iuwnhvov:e86m8BldW8Deo5FWsb-FJU-jYf1_N21d@eagle.rmq.cloudamqp.com/iuwnhvov')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print("Received in admin")
    id = json.loads(body)
    print(id)
    product = Products.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print("Product liked increased!")

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("Started Consuming....")

channel.start_consuming()

channel.close()
