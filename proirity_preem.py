# Function to calculate waiting time for Priority Scheduling (Preemptive)
def priority_preemptive(processes, arrivalTime, burstTime, priority):
    n = len(processes)
    remainingTime = burstTime[:]  # Copy of burstTime to track remaining execution time
    waitingTime = [0] * n
    completed = [False] * n
    currentTime = 0
    completedCount = 0

    while completedCount < n:
        # Find the process with the highest priority that has arrived
        idx = -1
        highestPriority = float('inf')
        for i in range(n):
            if not completed[i] and arrivalTime[i] <= currentTime and priority[i] < highestPriority:
                highestPriority = priority[i]
                idx = i

        if idx == -1:  # No process is ready, advance time
            currentTime += 1
            continue

        # Execute the selected process for 1 unit of time
        remainingTime[idx] -= 1
        currentTime += 1

        # If the process is completed
        if remainingTime[idx] == 0:
            completed[idx] = True
            completedCount += 1
            waitingTime[idx] = currentTime - arrivalTime[idx] - burstTime[idx]

    return waitingTime

# Function to calculate turnaround time
def calculateTurnaroundTime(burstTime, waitingTime):
    n = len(burstTime)
    turnaroundTime = [0] * n
    for i in range(n):
        turnaroundTime[i] = burstTime[i] + waitingTime[i]
    return turnaroundTime

# Function to calculate average times
def calculateAverageTimes(processes, arrivalTime, burstTime, priority):
    # Sort processes by arrival time
    zipped = sorted(zip(arrivalTime, burstTime, priority, processes), key=lambda x: x[0])
    sorted_arrivalTime = [item[0] for item in zipped]
    sorted_burstTime = [item[1] for item in zipped]
    sorted_priority = [item[2] for item in zipped]
    sorted_processes = [item[3] for item in zipped]

    waitingTime = priority_preemptive(sorted_processes, sorted_arrivalTime, sorted_burstTime, sorted_priority)
    turnaroundTime = calculateTurnaroundTime(sorted_burstTime, waitingTime)

    avgWaitingTime = sum(waitingTime) / len(sorted_processes)
    avgTurnaroundTime = sum(turnaroundTime) / len(sorted_processes)

    print("\nProcess\tArrival Time\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(len(sorted_processes)):  # Print in sorted order
        print(f"{sorted_processes[i]}\t\t{sorted_arrivalTime[i]}\t\t{sorted_burstTime[i]}\t\t{sorted_priority[i]}\t\t{waitingTime[i]}\t\t{turnaroundTime[i]}")

    print(f"\nAverage Waiting Time: {avgWaitingTime:.2f}")
    print(f"Average Turnaround Time: {avgTurnaroundTime:.2f}")

# Function to accept user input and display results
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

    print("\nPriority Scheduling (Preemptive) Algorithm with User Input:")
    calculateAverageTimes(processes, arrivalTime, burstTime, priority)

# Main function
if __name__ == "__main__":
    acceptDisplay()
