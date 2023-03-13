
import random


lower="abcdefghijklmnñopqrstuvwxyz"

upper="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

numbers="0123456789"

sybols="!#$%&?_-"

conjunto=lower+upper+numbers+sybols
length=10

password="".join(random.sample(conjunto,length))

print(password)