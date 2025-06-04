i=1
while i>0:
    user = input("What would you like to do? Input a Number: \n 1. Add a task \n 2. Show tasks \n 3. Exit")
    if user == "1":
        creation = input("What is your task?")
        with open("tasks.txt", "a") as f:
            f.write(creation+"\n")
            print('Task was added.')
    elif user == "2":
        with open("tasks.txt", "r") as f:
            content = f.read()
            print(content)
    else:
        print('Exiting.')
        break
