# Function to calculate waiting time and start time for Priority Scheduling (Non-Preemptive)
def priority_non_preemptive(processes, arrivalTime, burstTime, priority):
    n = len(processes)
    waitingTime = [0] * n
    startTime = [0] * n
    completed = [False] * n
    currentTime = 0
    completedCount = 0

    while completedCount < n:
        idx = -1
        highestPriority = float('inf')

        # Find the process with the highest priority among arrived processes
        for i in range(n):
            if not completed[i] and arrivalTime[i] <= currentTime and priority[i] < highestPriority:
                highestPriority = priority[i]
                idx = i

        if idx == -1:
            currentTime += 1
            continue

        startTime[idx] = currentTime
        waitingTime[idx] = currentTime - arrivalTime[idx]
        currentTime += burstTime[idx]
        completed[idx] = True
        completedCount += 1

    return waitingTime, startTime

# Function to calculate turnaround time
def calculateTurnaroundTime(burstTime, waitingTime):
    n = len(burstTime)
    turnaroundTime = [0] * n
    for i in range(n):
        turnaroundTime[i] = burstTime[i] + waitingTime[i]
    return turnaroundTime

# Function to print Gantt Chart
def printGanttChart(processes, startTime, burstTime):
    print("\nGantt Chart:")
    
    # Top bar
    print(" ", end="")
    for i in range(len(processes)):
        print("------", end="")
    print()

    # Process names in the middle
    print("|", end="")
    for i in range(len(processes)):
        print(f"  {processes[i]}  |", end="")
    print()

    # Bottom bar
    print(" ", end="")
    for i in range(len(processes)):
        print("------", end="")
    print()

    # Time line
    time = startTime[0]
    print(f"{time:>2}", end="   ")
    for i in range(len(processes)):
        time = startTime[i] + burstTime[i]
        print(f"{time:>2}   ", end="")
    print("\n")

# Function to calculate averages and display all results
def calculateAverageTimes(processes, arrivalTime, burstTime, priority):
    # Sort all inputs by arrival time
    zipped = sorted(zip(arrivalTime, burstTime, priority, processes), key=lambda x: x[0])
    sorted_arrivalTime = [item[0] for item in zipped]
    sorted_burstTime = [item[1] for item in zipped]
    sorted_priority = [item[2] for item in zipped]
    sorted_processes = [item[3] for item in zipped]

    # Get waiting time and start time
    waitingTime, startTime = priority_non_preemptive(sorted_processes, sorted_arrivalTime, sorted_burstTime, sorted_priority)

    # Get turnaround time
    turnaroundTime = calculateTurnaroundTime(sorted_burstTime, waitingTime)

    # Calculate averages
    avgWaitingTime = sum(waitingTime) / len(sorted_processes)
    avgTurnaroundTime = sum(turnaroundTime) / len(sorted_processes)

    # Display results
    print("\nProcess\tArrival Time\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(len(sorted_processes)):
        print(f"{sorted_processes[i]}\t\t{sorted_arrivalTime[i]}\t\t{sorted_burstTime[i]}\t\t{sorted_priority[i]}\t\t{waitingTime[i]}\t\t{turnaroundTime[i]}")

    # Print Gantt chart
    printGanttChart(sorted_processes, startTime, sorted_burstTime)

    # Print averages
    print(f"Average Waiting Time: {avgWaitingTime:.2f}")
    print(f"Average Turnaround Time: {avgTurnaroundTime:.2f}")

# Function to accept user input and run scheduling
def acceptDisplay():
    # Accept number of processes
    n = int(input("Enter the number of processes: "))

    # Accept process IDs
    processes = []
    for i in range(n):
        processes.append(input(f"Enter Process ID for process {i+1}: "))

    # Accept arrival times
    arrivalTime = []
    for i in range(n):
        arrivalTime.append(int(input(f"Enter Arrival Time for process {processes[i]}: ")))

    # Accept burst times
    burstTime = []
    for i in range(n):
        burstTime.append(int(input(f"Enter Burst Time for process {processes[i]}: ")))

    # Accept priority values
    priority = []
    for i in range(n):
        priority.append(int(input(f"Enter Priority for process {processes[i]} (Lower number = Higher priority): ")))

    # Display results
    print("\nPriority Scheduling (Non-Preemptive) Algorithm with User Input:")
    calculateAverageTimes(processes, arrivalTime, burstTime, priority)

# Main function
if __name__ == "__main__":
    acceptDisplay()
