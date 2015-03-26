#
#   Fanout Exchange
# 

import pika
import sys

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print " [x] Send %r" % ( message,)
connection.close()