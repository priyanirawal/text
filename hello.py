with open("tasks.txt", "a") as f:
    f.write("finish chapter 3"+ "\n")
with open("tasks.txt", "r") as f:
    content = f.read()
print(content)
