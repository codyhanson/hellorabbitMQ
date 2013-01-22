#!/usr/bin/env python
import sys
import pika #for talking AMQP


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


#declare a new queue
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Default message!"

#send a message
channel.basic_publish( exchange='', routing_key='task_queue', body=message)
print " [x] Sent {0}".format(message)

connection.close()
