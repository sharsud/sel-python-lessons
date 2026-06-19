# #math
#
# import math
# print(math.pi)
#
# print(math.sqrt(25))
#
# import random as rnd
# print(rnd.random())
# print(rnd.randint(1,10))

#userdefined module
# import utils
# print(utils.greet("Psudo"))
#
# from calculator.mathOperations.calculator import add
# print(add(1, 2))
#
#
# import os
# print(os.getcwd())
# print(os.listdir())
#
# import datetime
# now=datetime.datetime.now()
# print(now)
# tomorrow=now+datetime.timedelta(days=1)
# print(tomorrow)

import json
data={"name":"Psudo", "location":"India"}
jsonData=json.dumps(data)
print(jsonData)
print(type(jsonData))
parceddata=json.loads(jsonData)
print(parceddata)
print(type(parceddata))


#numpy  pandas request


import importlib
import utils
importlib.reload(utils)