import json 

codigo = "124553"
confx ="""{"conf":{"codigo" : ""}}"""

con1 = json.loads(confx)
con1['codigo']="123456"
print(con1)


print( confx)