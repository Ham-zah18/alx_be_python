Task = input("Enter a single task: ")
Priority = input("choose a priority (high/medium/low): ")
Time_bound = input("Is the task time-bound (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate atttention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task that requires your attention.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task. Remember to complete it this week!")
        else:
            print(f"Reminder: '{task}' is a medium priority task, Remember to check.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task. Consider completing it later today!")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Please choose a valid task priority")

