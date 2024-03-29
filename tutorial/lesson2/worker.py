#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#declare a new queue
channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties,body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.'))
    print " [X] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,queue='task_queue')

print "[*] Waiting for messages. ctrl-c to exit"
channel.start_consuming()
