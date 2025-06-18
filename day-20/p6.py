import json
inp = '{"name": "Alice","age":30}'

#json obj string converted into Dictionary format
#result should be {"name":"Alice","age":30}

# n=eval(inp)
result = json.loads(inp)
result=json.dumps(inp) #converted dict into string
print(result["name"])
