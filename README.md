# redis-LIFO-queue-object-store
Python implementation of fixed length FIFO queue in Redis. Useful for timestamp based sliding window cache in real time streaming applications.

REDIS Sliding window implementation.
Use Sliding window for Caching data captured using Realtime APIs. Write data to REDIS for faster data delivery using APIs.

SlidingWindow takes as input the name of the queue the client will write data to, and the length of queue.
Insert objects into queue using the insertObject() -> This function puts the key into the queue, and creates a seperate key-value pair in REDIS.

getObjects() retrieves all contents in the queue. The content represents keys in REDIS corresponding to data in the sliding window. 
