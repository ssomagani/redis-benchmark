import redis,random
r = redis.Redis(host='localhost', port=6379, db=0)

productCount = 20
userCount = 100

for x in range(productCount):
    r.hmset(F"product:{x}", {"cost": random.randint(5,10)})

for x in range(userCount):
    r.hmset(F"balance:{x}", {"balance": random.randint(50,500)})
    r.hmset(F"user:{x}", {"user_blob": "asdfghj"})
    for y in range(productCount):
        r.hmset(F"usage:{x}:{y}", {"alloc_units":0})
 
