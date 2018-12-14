import redisSlidingWindow

print ("TEST")

db = redisSlidingWindow.SlidingWindow()


#Reset all memory
db.deleteAll()


db.insertObject("8", {"val" :"One"})

print(db.getObjects())