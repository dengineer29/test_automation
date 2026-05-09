import printjob

queue = printjob.PrintQueue()

while True:

    # 1. Show the menu
    print("\n===== Print Queue Manager =====")
    print("1. Add job")
    print("2. View queue")
    print("3. Cancel job")
    print("4. Process next job")
    print("q. Quit")

    # 2. Wait for input
    choice = input("> ")

    # 3. React to choice
    if choice == "1":
        # ask for job details, create job, add to queue
        user = input("Username: ")
        filename = input("Filename: ") 
        size = input("File size: ")  
        date = input("Date: ") 
        printer = input("Printer: ")
        color = input("Color: ")

        job = printjob.ColorPrintJob(user, filename, size, date, printer, color)
        queue.add(job)

    elif choice == "2":
        # loop through queue and print each job
        queue.print_jobList()

    elif choice == "3":
        # ask which job index, call cancel on it
        pass

    elif choice == "4":
        # call queue.process() — render and remove first job
        pass

    elif choice == "q":
        print("Goodbye.")
        break  # exits the while loop

    else:
        print("Invalid choice. Try again.")