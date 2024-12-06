from task import Task

#want user to be prompted for task, calculate the priority of that task, and output the current priority
def main():
    #three main methods:
    """get the tasks, calculate the priority of those tasks(there are other tasks in the list), provide
    the output of the tasks in order of priority"""
    tasks = get_tasks()
    sorted_tasks = calculatePriority(tasks)

    print("\nSorted Task List:")

    for task in sorted_tasks:
        print(task)

    print("\nTask Allocation for Today (12-hour limit):")

    daily_schedule = allocate_schedule(sorted_tasks, daily_limit=12)
    for item in daily_schedule:
        print(item)

def get_tasks():
    task_list = []
    print("Enter tasks (type 'done' when finished):")
    while True:
        name = input("Task name: ")
        if name.lower() == "done":
            break
        try:
            deadline = input("Deadline (YYYY-MM-DD): ")
            hardness = int(input("Hardness level (1-5): "))
            duration = int(input("Estimated duration (hours): "))

            # Validate inputs
            if hardness < 1 or hardness > 5:
                print("Hardness level must be between 1 and 5.")
                continue
            if duration <= 0:
                print("Duration must be a positive number.")
                continue

            task_list.append(Task(name, deadline, hardness, duration))
        except ValueError:
            print("Invalid input. Please try again.")
    return task_list
    

def calculatePriority(tasks):
    return sorted(tasks, key=lambda t:(t.priority_score, t.days_remaining, t.hardness_level))
    


def allocate_schedule(tasks, daily_limit=12):
    schedule = []
    remaining_hours = daily_limit

    for task in tasks:
        if task.estimated_duration <= remaining_hours:
            schedule.append(task)
            remaining_hours -= task.estimated_duration
        else:
            # Allocate partial hours if the task cannot fully fit into the day's schedule
            schedule.append(f"Partial: {task.name} ({remaining_hours} hours)")
            break

    return schedule

    




if __name__ == "__main__":
    print("Welcome to the Student Task Scheduler!")
    main()
