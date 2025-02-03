# Function to calculate waiting time for Round Robin Scheduling
def round_robin(processes, arrivalTime, burstTime, timeQuantum):
    n = len(processes)
    remainingTime = burstTime[:]  # Copy of burstTime to track remaining execution time
    waitingTime = [0] * n
    currentTime = 0
    queue = []
    
    # Sort processes by arrival time
    sorted_processes = sorted(zip(arrivalTime, burstTime, processes), key=lambda x: x[0])
    arrivalTime, burstTime, processes = zip(*sorted_processes)
    remainingTime = list(burstTime)

    # Add first process to queue
    index = 0
    while index < n and arrivalTime[index] <= currentTime:
        queue.append(index)
        index += 1

    while queue:
        idx = queue.pop(0)

        # Execute process for at most time quantum
        executionTime = min(timeQuantum, remainingTime[idx])
        remainingTime[idx] -= executionTime
        currentTime += executionTime

        # Add waiting time
        waitingTime[idx] = currentTime - arrivalTime[idx] - (burstTime[idx] - remainingTime[idx])

        # Add new processes that have arrived
        while index < n and arrivalTime[index] <= currentTime:
            queue.append(index)
            index += 1

        # If process is not finished, put it back in the queue
        if remainingTime[idx] > 0:
            queue.append(idx)

    return waitingTime

# Function to calculate turnaround time
def calculateTurnaroundTime(burstTime, waitingTime):
    n = len(burstTime)
    turnaroundTime = [0] * n
    for i in range(n):
        turnaroundTime[i] = burstTime[i] + waitingTime[i]
    return turnaroundTime

# Function to calculate average times
def calculateAverageTimes(processes, arrivalTime, burstTime, timeQuantum):
    # Sort processes by arrival time
    zipped = sorted(zip(arrivalTime, burstTime, processes), key=lambda x: x[0])
    sorted_arrivalTime = [item[0] for item in zipped]
    sorted_burstTime = [item[1] for item in zipped]
    sorted_processes = [item[2] for item in zipped]

    waitingTime = round_robin(sorted_processes, sorted_arrivalTime, sorted_burstTime, timeQuantum)
    turnaroundTime = calculateTurnaroundTime(sorted_burstTime, waitingTime)

    avgWaitingTime = sum(waitingTime) / len(sorted_processes)
    avgTurnaroundTime = sum(turnaroundTime) / len(sorted_processes)

    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(len(sorted_processes)):  # Print in sorted order
        print(f"{sorted_processes[i]}\t\t{sorted_arrivalTime[i]}\t\t{sorted_burstTime[i]}\t\t{waitingTime[i]}\t\t{turnaroundTime[i]}")

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

    # Accept time quantum
    timeQuantum = int(input("Enter Time Quantum: "))

    print("\nRound Robin Scheduling Algorithm with User Input:")
    calculateAverageTimes(processes, arrivalTime, burstTime, timeQuantum)

# Main function
if __name__ == "__main__":
    acceptDisplay()
