posts=[
    {"user":"alice","post":"hi"},
    {"user":"bob","post":"hello"},
    {"user":"alice","post":"again"},
    {"user":"x","post":"xyz"},
    {"user":"alice","post":"again"}
]
count={}
for i in posts:
    user=i['user']
    count[user]=count.get(user,0)+1
print(count)
user=input()
for i in user:
    if id in posts:
        count[user]=count.get(user,0)+1
        print(user)