lines = 0
i=1
while i>0:
    user = input("What would you like to do? Input a Number: \n 1. Add a task \n 2. Show tasks \n 3. Count the number of tasks \n 4. Delete task \n 5. Mark task as complete \n 6. Exit\n")
    if user == "1":
        creation = input("What is your task?")
        with open("tasks.txt", "r", encoding="utf-8") as f:
            lines = len(f.readlines())
        with open("tasks.txt", "a", encoding="utf-8") as f:
            f.write(str(lines+1)+". "+creation+"\n")
            print('Task was added.')
    elif user == "2":
        with open("tasks.txt", "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
    elif user == "3":
        with open("tasks.txt", "r", encoding="utf-8") as f:
            total_lines = f.readlines()
            print("The number of tasks in your list are:", len(total_lines))
    elif user == "4":
        with open("tasks.txt", "r+", encoding="utf-8") as f:
            num_tasks = f.readlines()
            deletion = int(input("What number task do you want to delete?\n"))
            if 1 <= deletion <= len(num_tasks):
                del num_tasks[deletion-1]
                with open("tasks.txt", "w", encoding="utf-8") as f:
                    for i, task in enumerate(num_tasks):
                        new_num = task.split(". ")
                        last_element = new_num[1]
                        f.write(str(i+1)+". "+last_element)
                    print("Task number",deletion,"was deleted.")

            else:
                print("Invalid task number.")
    elif user == "5":
        with open("tasks.txt", "r", encoding="utf-8") as f:
            task_list = f.readlines() 
            completion = int(input("What is the number of the task you completed?"))
            if 1 <= completion <= len(task_list):
                task_list[completion - 1] = task_list[completion - 1].strip() + " ✅\n"
                with open("tasks.txt", "w", encoding="utf-8") as f:
                    f.writelines(task_list)
                    print("Task " + str(completion) + " marked as complete.")
            else:
                print("Invalid task number.")

    else:
        print('Exiting.')
        break
