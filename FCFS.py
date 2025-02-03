# Function to calculate waiting time
def Fcfs(processes, arrivalTime, burstTime):
    n = len(processes)
    waitingTime = [0] * n
    startTime = [0] * n  # Time at which process starts execution

    # First process starts at its arrival time
    startTime[0] = arrivalTime[0]
    waitingTime[0] = 0  # First process has no waiting time

    for i in range(1, n):
        # Calculate the service time of the current process
        startTime[i] = max(startTime[i - 1] + burstTime[i - 1], arrivalTime[i])
        # Calculate waiting time
        waitingTime[i] = startTime[i] - arrivalTime[i]
    
        # If waiting time is negative, set it to 0
        waitingTime[i] = max(waitingTime[i], 0)
    
    return waitingTime

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
    # arrivalTime, burstTime, processes = zip(*zipped)
    sorted_arrivalTime = [item[0] for item in zipped]
    sorted_burstTime = [item[1] for item in zipped]
    sorted_processes = [item[2] for item in zipped]

    waitingTime = Fcfs(sorted_processes, sorted_arrivalTime, sorted_burstTime)
    turnaroundTime = calculateTurnaroundTime(sorted_burstTime, waitingTime)

    avgWaitingTime = sum(waitingTime) / len(sorted_processes)
    avgTurnaroundTime = sum(turnaroundTime) / len(sorted_processes)
    
    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(len(sorted_processes)):
        print(f"{sorted_processes[i]}\t\t{sorted_arrivalTime[i]}\t\t{sorted_burstTime[i]}\t\t{waitingTime[i]}\t\t{turnaroundTime[i]}")
    
    print(f"\nAverage Waiting Time: {avgWaitingTime:.2f}")
    print(f"Average Turnaround Time: {avgTurnaroundTime:.2f}")




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
    
    print("\nFCFS Scheduling Algorithm with User Input:")
    calculateAverageTimes(processes, arrivalTime, burstTime)

# Main function
if __name__ == "__main__":
    acceptDisplay()

