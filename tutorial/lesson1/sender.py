#!/usr/bin/env python

import pika #for talking AMQP

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#declare a new queue
channel.queue_declare(queue='hello')

#send a message
channel.basic_publish( exchange='',
                       routing_key='hello',
                       body='hello world!')

print " [x] Sent 'hello World!'"

connection.close()
