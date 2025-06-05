lines = 0
i=1
while i>0:
    user = input("What would you like to do? Input a Number: \n 1. Add a task \n 2. Show tasks \n 3. Count the number of tasks \n 4. Delete task \n 5. Exit\n")
    if user == "1":
        creation = input("What is your task?")
        with open("tasks.txt", "r") as f:
            lines = len(f.readlines())
        with open("tasks.txt", "a") as f:
            f.write(str(lines+1)+". "+creation+"\n")
            print('Task was added.')
    elif user == "2":
        with open("tasks.txt", "r") as f:
            content = f.read()
            print(content)
    elif user == "3":
        with open("tasks.txt", "r") as f:
            total_lines = f.readlines()
            print("The number of tasks in your list are:", len(total_lines))
    elif user == "4":
        with open("tasks.txt", "r+") as f:
            num_tasks = f.readlines()
            deletion = int(input("What number task do you want to delete?\n"))
            print(deletion)
            print(num_tasks)
            if 1 <= deletion <= len(num_tasks):
                del num_tasks[deletion-1]
                with open("tasks.txt", "w") as f:
                    for i, task in enumerate(num_tasks):
                        new_num = task.split(". ")
                        last_element = new_num[1]
                        f.write(str(i+1)+". "+last_element)
                    print("Task number",deletion,"was deleted.")

            else:
                print("Invalid task number.")
    else:
        print('Exiting.')
        break
