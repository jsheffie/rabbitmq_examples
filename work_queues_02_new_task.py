import pika 
import sys

connection_parms = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parms)

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True) # still a named queue

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange='', routing_key='task_queue', body=message ,
	                  properties=pika.BasicProperties(delivery_mode=2, # make the message persistant
	                  ))

print " [x] Sent %r" % ( message, )

connection.close()
