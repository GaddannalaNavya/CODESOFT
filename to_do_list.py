tasks = []

def addTask():
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def listTask():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks:")    
        for index, task in enumerate(tasks):
            print(f"tasks #{index}. {task}")

def deleteTask():
    listTask()
    if tasks:
        try:
            taskToDelete= int(input("Enter the number of the task you want to delete: "))
            if taskToDelete >= 0 and taskToDelete < len(tasks):
                tasks.pop(taskToDelete)
                print(f"Task {taskToDelete} has been removed.")
            else:
                print(f"Task #{taskToDelete}was not found.")
        except:
            print("Invalid input.")

if __name__ == "__main__":
    print("Welcome to the to do list:")
    while True:
        print("\n")
        print("please select one of the following options")
        print("__________________________________________")
        print("1.Add a new task")
        print("2.Delete a task")
        print("3.List tasks")
        print("4.Quit")
        choice =input("Enter your choice: ")
        if(choice=="1"):
            addTask()
        elif(choice=="2"):
            deleteTask()
        elif(choice=="3"):
            listTask()
        elif(choice=="4"):
            break
        else:
            ("Invalid Input.Please try again.")
    print("Bye Bye")        
