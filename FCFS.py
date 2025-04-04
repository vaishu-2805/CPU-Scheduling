# Function to calculate waiting time
def Fcfs(processes, arrivalTime, burstTime):
    n = len(processes)
    waitingTime = [0] * n
    startTime = [0] * n  # Time at which process starts execution

    # First process starts at its arrival time
    startTime[0] = arrivalTime[0]
    waitingTime[0] = 0  # First process has no waiting time

    for i in range(1, n):
        startTime[i] = max(startTime[i - 1] + burstTime[i - 1], arrivalTime[i])
        waitingTime[i] = startTime[i] - arrivalTime[i]
        waitingTime[i] = max(waitingTime[i], 0)

    return waitingTime, startTime

# Function to calculate turnaround time
def calculateTurnaroundTime(burstTime, waitingTime):
    return [bt + wt for bt, wt in zip(burstTime, waitingTime)]

# Function to generate Gantt chart
def printGanttChart(processes, startTime, burstTime):
    print("\nGantt Chart:")
    print(" ", end="")
    for i in range(len(processes)):
        print("------", end="")
    print()

    print("|", end="")
    for i in range(len(processes)):
        print(f"  {processes[i]}  |", end="")
    print()

    print(" ", end="")
    for i in range(len(processes)):
        print("------", end="")
    print()

    time = startTime[0]
    print(f"{time:>2}", end="   ")
    for i in range(len(burstTime)):
        time = startTime[i] + burstTime[i]
        print(f"{time:>2}   ", end="")
    print("\n")

# Function to calculate and display everything
def calculateAverageTimes(processes, arrivalTime, burstTime):
    # Sort by arrival time
    zipped = sorted(zip(arrivalTime, burstTime, processes), key=lambda x: x[0])
    arrivalTime = [item[0] for item in zipped]
    burstTime = [item[1] for item in zipped]
    processes = [item[2] for item in zipped]

    waitingTime, startTime = Fcfs(processes, arrivalTime, burstTime)
    turnaroundTime = calculateTurnaroundTime(burstTime, waitingTime)

    avgWaitingTime = sum(waitingTime) / len(processes)
    avgTurnaroundTime = sum(turnaroundTime) / len(processes)

    print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround")
    for i in range(len(processes)):
        print(f"{processes[i]}\t{arrivalTime[i]}\t{burstTime[i]}\t{waitingTime[i]}\t{turnaroundTime[i]}")

    printGanttChart(processes, startTime, burstTime)

    print(f"Average Waiting Time: {avgWaitingTime:.2f}")
    print(f"Average Turnaround Time: {avgTurnaroundTime:.2f}")

# Function to accept and display data
def acceptDisplay():
    n = int(input("Enter the number of processes: "))
    processes = [input(f"Enter Process ID for process {i+1}: ") for i in range(n)]
    arrivalTime = [int(input(f"Enter Arrival Time for process {processes[i]}: ")) for i in range(n)]
    burstTime = [int(input(f"Enter Burst Time for process {processes[i]}: ")) for i in range(n)]

    print("\nFCFS Scheduling Algorithm Output:")
    calculateAverageTimes(processes, arrivalTime, burstTime)

# Main function
if __name__ == "__main__":
    acceptDisplay()
