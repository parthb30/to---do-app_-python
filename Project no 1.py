tasks = []
while True:
   print("\n1. Add a task")
   print("2. View a tasks")
   print("3. Delete a task")
   print("4. Exit")

   choice = input("Enter your choice:")
   
   if choice == "1":
         task = input("Enter the task:")
         tasks.append(task)
         print ("Task added successfully!")
   
   elif choice == "2": 
        if len(tasks) <= 0:
             print("No tasks are available")
        else:
             for i in range(len(tasks)):
              print(i, tasks[i])
                       
   
   elif choice == "3":
        index = int(input("Enter the index of the task to delete:"))
        
        if index >= 0 and index < len(tasks):    
            tasks.pop(index)
            print("Task deleted successfully!")
        else:
            print("Invalid index!, please try again.")

   elif choice == "4":
        print("You have exited the program.")
        break
   

     
        