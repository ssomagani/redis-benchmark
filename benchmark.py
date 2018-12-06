import redis,random
r = redis.Redis(host='localhost', port=6379, db=0)

productCount = 20
userCount = 100

for x in range(5):
    products = []
    for y in range(productCount):
        usage = r.hget(F"usage:{x}:{y}", "alloc_units")
        products.append(F"{y}:{usage}")
    print({**r.hgetall(F"user:{x}"), **{"products":products}, **r.hgetall(F"balance:{x}")})

