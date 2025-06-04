user = input("Write down a task.")
with open("tasks.txt", "a") as f:
    f.write(user+"\n")
with open("tasks.txt", "r") as f:
    content = f.read()
print(content)
