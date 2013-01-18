#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#declare a new queue
channel.queue_declare(queue='hello')

def callback(ch, method, properties,body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,queue='hello',no_ack=True)

print "[*] Waiting for messages. ctrl-c to exit"
channel.start_consuming()
