i=1
while i>0:
    user = input("What would you like to do? Input a Number: \n 1. Add a task \n 2. Show tasks \n 3. Count the number of tasks \n 4. Exit\n")
    if user == "1":
        creation = input("What is your task?")
        with open("tasks.txt", "a") as f:
            f.write(creation+"\n")
            print('Task was added.')
    elif user == "2":
        with open("tasks.txt", "r") as f:
            content = f.read()
            print(content)
    elif user == "3":
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
            print("The number of tasks in your list are:", len(lines))
    else:
        print('Exiting.')
        break
