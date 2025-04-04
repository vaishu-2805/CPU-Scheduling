# Function to calculate waiting time and generate Gantt Chart for Round Robin Scheduling
def round_robin(processes, arrivalTime, burstTime, timeQuantum):
    n = len(processes)
    remainingTime = burstTime[:]
    waitingTime = [0] * n
    completionTime = [0] * n
    currentTime = 0
    queue = []
    execution_order = []

    # Sort by arrival time
    sorted_data = sorted(zip(arrivalTime, burstTime, processes), key=lambda x: x[0])
    arrivalTime, burstTime, processes = zip(*sorted_data)
    arrivalTime = list(arrivalTime)
    burstTime = list(burstTime)
    processes = list(processes)
    remainingTime = list(burstTime)

    visited = [False] * n
    index = 0

    # Add first process to queue if arrived at time 0
    while index < n and arrivalTime[index] <= currentTime:
        queue.append(index)
        visited[index] = True
        index += 1

    if not queue:
        queue.append(0)
        visited[0] = True
        currentTime = arrivalTime[0]

    while queue:
        idx = queue.pop(0)

        # Execute the process
        executionTime = min(timeQuantum, remainingTime[idx])
        execution_order.append((processes[idx], currentTime, currentTime + executionTime))
        currentTime += executionTime
        remainingTime[idx] -= executionTime

        # Check new arrivals during execution
        for i in range(n):
            if not visited[i] and arrivalTime[i] <= currentTime:
                queue.append(i)
                visited[i] = True

        # If process not complete, re-add to queue
        if remainingTime[idx] > 0:
            queue.append(idx)
        else:
            completionTime[idx] = currentTime
            waitingTime[idx] = completionTime[idx] - arrivalTime[idx] - burstTime[idx]

    return waitingTime, execution_order

# Function to calculate turnaround time
def calculateTurnaroundTime(burstTime, waitingTime):
    return [burstTime[i] + waitingTime[i] for i in range(len(burstTime))]

# Function to print Gantt Chart
def printGanttChart(execution_order):
    print("\nGantt Chart:")
    
    # Top bar
    print(" ", end="")
    for p, st, et in execution_order:
        print("----", end="")
    print()

    # Process IDs
    print("|", end="")
    for p, st, et in execution_order:
        print(f" {p} |", end="")
    print()

    # Bottom bar
    print(" ", end="")
    for p, st, et in execution_order:
        print("----", end="")
    print()

    # Timeline
    print()
    for p, st, et in execution_order:
        print(f"{st:<4}", end="")
    print(f"{execution_order[-1][2]}")  # Last end time

# Function to calculate average times and print all data
def calculateAverageTimes(processes, arrivalTime, burstTime, timeQuantum):
    waitingTime, execution_order = round_robin(processes, arrivalTime, burstTime, timeQuantum)
    turnaroundTime = calculateTurnaroundTime(burstTime, waitingTime)

    avgWaitingTime = sum(waitingTime) / len(processes)
    avgTurnaroundTime = sum(turnaroundTime) / len(processes)

    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(f"{processes[i]}\t\t{arrivalTime[i]}\t\t{burstTime[i]}\t\t{waitingTime[i]}\t\t{turnaroundTime[i]}")

    printGanttChart(execution_order)

    print(f"\nAverage Waiting Time: {avgWaitingTime:.2f}")
    print(f"Average Turnaround Time: {avgTurnaroundTime:.2f}")

# Function to take user input and display results
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

    timeQuantum = int(input("Enter Time Quantum: "))

    print("\nRound Robin Scheduling Algorithm with User Input:")
    calculateAverageTimes(processes, arrivalTime, burstTime, timeQuantum)

# Main function
if __name__ == "__main__":
    acceptDisplay()
