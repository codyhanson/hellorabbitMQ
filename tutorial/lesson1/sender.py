#!/usr/bin/env python

import sys
import pika #for talking AMQP

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#declare a new queue
channel.queue_declare(queue='hello')

#send a message
for i in range(int(sys.argv[1])):
    bodystr = 'hello {0}!'.format(i)
    channel.basic_publish( exchange='', routing_key='hello', body=bodystr)
    print " [x] Sent {0}".format(bodystr)


connection.close()
