import Day1.printjob as printjob

queue = printjob.PrintQueue()             # create one shared queue for the whole session

while True:

    # show the menu each loop iteration
    print("\n===== Print Queue Manager =====")
    print(f"Jobs in queue: {queue.get_queue_size()}")   # show queue size in the header so user always knows
    print("1. Add job")
    print("2. View queue")
    print("3. Cancel job")
    print("4. Process next job")
    print("q. Quit")

    choice = input("> ")

    if choice == "1":
        # ask for job type first so both ColorPrintJob and BWPrintJob are reachable
        color_mode = input("Job type (color/bw): ").strip().lower()

        # collect fields common to both job types
        user = input("Username: ")
        filename = input("Filename: ")
        size = input("File size: ")
        date = input("Date: ")
        printer = input("Printer: ")
        pages = input("Enter number of pages: ")
        

        if color_mode == "color":
            color_type = input("Color: ")                              # only ask for color if it's a color job
            job = printjob.ColorPrintJob(user, filename, size, date, printer, color_mode, color_type, pages)
        elif color_mode == "bw":
            job = printjob.BWPrintJob(user, filename, size, date, printer, color_mode, pages)   # no color needed for BW
        else:
            print("Unknown job type. Please enter 'color' or 'bw'.")
            continue                                               # skip the rest and show menu again

        queue.add(job)
        print(f"Job '{filename}' added to queue.")                # confirm the add — don't dump the whole list

    elif choice == "2":
        # show all jobs with index numbers and current status
        queue.print_jobList()

    elif choice == "3":
        # show the queue first so the user knows which index to pick
        queue.print_jobList()

        if not queue.is_empty():                                  # only ask for input if there's something to cancel
            try:
                index = int(input("Enter job number to cancel: "))   # convert input to int for the index
                message = queue.cancel(index)                         # cancel() returns the cancel message
                print(message)
            except ValueError:
                print("Please enter a valid number.")             # handles the case where user types letters

    elif choice == "4":
        # process and remove the first job in the queue
        result = queue.process_next()                             # returns the job's process() output or empty message
        print(result)

    elif choice == "q":
        print("Goodbye.")
        break

    else:
        print("Invalid choice. Try again.")
