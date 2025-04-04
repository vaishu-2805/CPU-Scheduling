# Function to calculate waiting time and store execution history for Gantt Chart
def priority_preemptive(processes, arrivalTime, burstTime, priority):
    n = len(processes)
    remainingTime = burstTime[:]  # Copy burst time to track remaining time
    waitingTime = [0] * n
    completed = [False] * n
    currentTime = 0
    completedCount = 0
    startTime = [-1] * n
    execution_order = []

    while completedCount < n:
        idx = -1
        highestPriority = float('inf')

        # Select the highest priority process that has arrived and is not completed
        for i in range(n):
            if arrivalTime[i] <= currentTime and not completed[i] and priority[i] < highestPriority:
                highestPriority = priority[i]
                idx = i

        if idx == -1:
            currentTime += 1
            continue

        # Log execution for Gantt Chart
        execution_order.append(processes[idx])

        # Record first start time
        if startTime[idx] == -1:
            startTime[idx] = currentTime

        # Execute process for 1 unit
        remainingTime[idx] -= 1
        currentTime += 1

        # If process is completed
        if remainingTime[idx] == 0:
            completed[idx] = True
            completedCount += 1
            waitingTime[idx] = currentTime - arrivalTime[idx] - burstTime[idx]

    return waitingTime, startTime, execution_order

# Function to calculate turnaround time
def calculateTurnaroundTime(burstTime, waitingTime):
    turnaroundTime = [burstTime[i] + waitingTime[i] for i in range(len(burstTime))]
    return turnaroundTime

# Function to print Gantt Chart
def printGanttChart(execution_order):
    print("\nGantt Chart:")

    # Top bar
    print(" ", end="")
    for p in execution_order:
        print("----", end="")
    print()

    # Process names
    print("|", end="")
    for p in execution_order:
        print(f" {p} |", end="")
    print()

    # Bottom bar
    print(" ", end="")
    for p in execution_order:
        print("----", end="")
    print()

    # Timeline
    time = 0
    print("0", end="")
    for p in execution_order:
        time += 1
        print(f"   {time}", end="")
    print("\n")

# Function to calculate averages and print table
def calculateAverageTimes(processes, arrivalTime, burstTime, priority):
    zipped = sorted(zip(arrivalTime, burstTime, priority, processes), key=lambda x: x[0])
    sorted_arrivalTime = [item[0] for item in zipped]
    sorted_burstTime = [item[1] for item in zipped]
    sorted_priority = [item[2] for item in zipped]
    sorted_processes = [item[3] for item in zipped]

    waitingTime, startTime, execution_order = priority_preemptive(
        sorted_processes, sorted_arrivalTime, sorted_burstTime, sorted_priority
    )
    turnaroundTime = calculateTurnaroundTime(sorted_burstTime, waitingTime)

    avgWaitingTime = sum(waitingTime) / len(sorted_processes)
    avgTurnaroundTime = sum(turnaroundTime) / len(sorted_processes)

    print("\nProcess\tArrival Time\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(len(sorted_processes)):
        print(f"{sorted_processes[i]}\t\t{sorted_arrivalTime[i]}\t\t{sorted_burstTime[i]}\t\t{sorted_priority[i]}\t\t{waitingTime[i]}\t\t{turnaroundTime[i]}")

    printGanttChart(execution_order)

    print(f"Average Waiting Time: {avgWaitingTime:.2f}")
    print(f"Average Turnaround Time: {avgTurnaroundTime:.2f}")

# Function to take user input
def acceptDisplay():
    n = int(input("Enter the number of processes: "))

    processes = []
    for i in range(n):
        processes.append(input(f"Enter Process ID for process {i+1}: "))

    arrivalTime = []
    for i in range(n):
        arrivalTime.append(int(input(f"Enter Arrival Time for process {processes[i]}: ")))

    burstTime = []
    for i in range(n):
        burstTime.append(int(input(f"Enter Burst Time for process {processes[i]}: ")))

    priority = []
    for i in range(n):
        priority.append(int(input(f"Enter Priority for process {processes[i]} (Lower number = Higher priority): ")))

    print("\nPriority Scheduling (Preemptive) Algorithm with User Input:")
    calculateAverageTimes(processes, arrivalTime, burstTime, priority)

# Main function
if __name__ == "__main__":
    acceptDisplay()
