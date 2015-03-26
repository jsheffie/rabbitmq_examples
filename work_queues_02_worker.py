import pika 
import sys
import time

connection_parms = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True) # still a named queue

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
	print " [x] Received %r" % ( body, )
	time.sleep(body.count('.'))
	print " [x] Done"
	ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1) # dont hand more that one message to a worker ( at a time )
channel.basic_consume(callback, queue='task_queue') #no_ack=False

channel.start_consuming()