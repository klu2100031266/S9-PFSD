import json

a = '{ "name":"John", "age":30, "city":"New York"}'
b = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.loads(a)
z = json.dumps(b)
print(y["age"])
print(z)