# Function to calculate waiting time for SJF Non-Preemptive
def sjf_non_preemptive(processes, arrivalTime, burstTime):
    n = len(processes)
    waitingTime = [0] * n
    completionTime = [0] * n
    completed = [False] * n
    currentTime = 0
    completedCount = 0
    execution_order = []

    while completedCount < n:
        # Find the next process to execute (shortest burst time that has arrived)
        idx = -1
        minBurst = float('inf')
        for i in range(n):
            if not completed[i] and arrivalTime[i] <= currentTime and burstTime[i] < minBurst:
                minBurst = burstTime[i]
                idx = i

        if idx == -1:  # No process ready, advance time
            currentTime += 1
            continue

        # Record execution for Gantt chart
        execution_order.append((processes[idx], currentTime, currentTime + burstTime[idx]))

        # Execute process
        waitingTime[idx] = currentTime - arrivalTime[idx]
        currentTime += burstTime[idx]
        completed[idx] = True
        completedCount += 1
        completionTime[idx] = currentTime

    return waitingTime, execution_order

# Function to calculate turnaround time
def calculateTurnaroundTime(burstTime, waitingTime):
    return [burstTime[i] + waitingTime[i] for i in range(len(burstTime))]

# Function to print Gantt Chart
def printGanttChart(execution_order):
    print("\nGantt Chart:")
    print(" ", end="")
    for p, st, et in execution_order:
        print("----", end="")
    print()
    
    print("|", end="")
    for p, st, et in execution_order:
        print(f" {p} |", end="")
    print()
    
    print(" ", end="")
    for p, st, et in execution_order:
        print("----", end="")
    print()
    
    for p, st, et in execution_order:
        print(f"{st:<4}", end="")
    print(f"{execution_order[-1][2]}")

# Function to calculate average times and display results
def calculateAverageTimes(processes, arrivalTime, burstTime):
    waitingTime, execution_order = sjf_non_preemptive(processes, arrivalTime, burstTime)
    turnaroundTime = calculateTurnaroundTime(burstTime, waitingTime)

    avgWaitingTime = sum(waitingTime) / len(processes)
    avgTurnaroundTime = sum(turnaroundTime) / len(processes)

    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(f"{processes[i]}\t\t{arrivalTime[i]}\t\t{burstTime[i]}\t\t{waitingTime[i]}\t\t{turnaroundTime[i]}")

    printGanttChart(execution_order)

    print(f"\nAverage Waiting Time: {avgWaitingTime:.2f}")
    print(f"Average Turnaround Time: {avgTurnaroundTime:.2f}")

# Function to accept user input and display results
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
    
    print("\nSJF Non-Preemptive Scheduling Algorithm with User Input:")
    calculateAverageTimes(processes, arrivalTime, burstTime)

# Main function
if __name__ == "__main__":
    acceptDisplay()
