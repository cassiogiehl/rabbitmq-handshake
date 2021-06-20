import pika, sys, os

class Response:
    def send_response():
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='response')

        channel.basic_publish(exchange='', routing_key='response', body='Hi JS!!!')
        print(" [x] Sent 'Hi JS!!!'")
        connection.close()
