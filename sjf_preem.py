# Function to calculate waiting time for SJF Preemptive (SRTF)
def sjf_preemptive(processes, arrivalTime, burstTime):
    n = len(processes)
    remainingTime = burstTime[:]  # Copy burst time for remaining execution
    waitingTime = [0] * n
    completed = [False] * n
    currentTime = 0
    completedCount = 0
    processOrder = []  # Track execution order
    lastExecuted = -1  # Track last executed process to avoid duplicate entries
    startTime = [-1] * n  # Track first execution time for each process

    while completedCount < n:
        # Find process with shortest remaining time at current time
        idx = -1
        minRemaining = float('inf')
        for i in range(n):
            if not completed[i] and arrivalTime[i] <= currentTime and remainingTime[i] < minRemaining:
                minRemaining = remainingTime[i]
                idx = i

        if idx == -1:  # No process is ready, advance time
            currentTime += 1
            continue

        # Record start time for first execution of a process
        if startTime[idx] == -1:
            startTime[idx] = currentTime

        # Execute the selected process for 1 time unit
        remainingTime[idx] -= 1
        if lastExecuted != processes[idx]:  # Track execution order
            processOrder.append(processes[idx])
        lastExecuted = processes[idx]

        if remainingTime[idx] == 0:  # Process is completed
            completed[idx] = True
            completedCount += 1
            waitingTime[idx] = (currentTime + 1) - arrivalTime[idx] - burstTime[idx]

        currentTime += 1

    return waitingTime, processOrder

# Function to calculate turnaround time
def calculateTurnaroundTime(burstTime, waitingTime):
    n = len(burstTime)
    turnaroundTime = [0] * n
    for i in range(n):
        turnaroundTime[i] = burstTime[i] + waitingTime[i]
    return turnaroundTime

# Function to calculate average times
def calculateAverageTimes(processes, arrivalTime, burstTime):
    # Sort processes by arrival time
    zipped = sorted(zip(arrivalTime, burstTime, processes), key=lambda x: x[0])
    sorted_arrivalTime = [item[0] for item in zipped]
    sorted_burstTime = [item[1] for item in zipped]
    sorted_processes = [item[2] for item in zipped]

    waitingTime, processOrder = sjf_preemptive(sorted_processes, sorted_arrivalTime, sorted_burstTime)
    turnaroundTime = calculateTurnaroundTime(sorted_burstTime, waitingTime)

    avgWaitingTime = sum(waitingTime) / len(sorted_processes)
    avgTurnaroundTime = sum(turnaroundTime) / len(sorted_processes)

    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(len(sorted_processes)):  # Print in sorted order
        print(f"{sorted_processes[i]}\t\t{sorted_arrivalTime[i]}\t\t{sorted_burstTime[i]}\t\t{waitingTime[i]}\t\t{turnaroundTime[i]}")

    print(f"\nAverage Waiting Time: {avgWaitingTime:.2f}")
    print(f"Average Turnaround Time: {avgTurnaroundTime:.2f}")
    print(f"\nExecution Order: {' -> '.join(processOrder)}")  # Display execution order

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

    print("\nSJF Preemptive (SRTF) Scheduling Algorithm with User Input:")
    calculateAverageTimes(processes, arrivalTime, burstTime)

# Main function
if __name__ == "__main__":
    acceptDisplay()
