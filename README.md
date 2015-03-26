# rabbitmq_examples

From the main site:
http://www.rabbitmq.com/getstarted.html

All of the examples use the pika.BlockingConnection

Example 1: pika.BlockingConnection
           basic_publish, basic_consume

Example 2: pika.BlockingConnection
           basic_publish, basic_consume ( w/ durability and a basic_qos prefetch_count )
           Message ack's are back on.
           Persistance is on, dont use persistance, use publisher confirms.

https://www.rabbitmq.com/confirms.html  
https://raw.githubusercontent.com/rabbitmq/rabbitmq-java-client/master/test/src/com/rabbitmq/examples/ConfirmDontLoseMessages.java


Example 3: Pub/Sub... this is the fanout exchange example.
           Fanout Exchange is for mindless broadcasting
           pika.BlockingConnection
           basic_publish, basic_consume ( w/ exclusive queue declare) 
           This means a tempory queue gets created, and removed when the 
           consumer disconnects. 


Example 4: Direct exchange w/ filtering based on routing keys
           example... use this for multicasting patterns.


Example 5: Topic exchange w/ filtering based on source && filter.
           i.e. 
           example... use this for multicasting patterns.





Note: Fanout exchange ingores the routing_key parameter



Administering Rabbit: ( things covered in the tutorial)

$ sudo rabbitmqctl list_queues
$ sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged
$ sudo rabbitmqctl list_exchanges
$ sudo rabbitmqctl list_bindings



Also: From this blog: 
http://spring.io/blog/2010/08/19/building-rabbitmq-apps-using-python/

Contains an example of an Fanout Exchange using the pika.AsynchcoreConnection

