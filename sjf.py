# Function to calculate waiting time for SJF Non-Preemptive
def sjf_non_preemptive(processes, arrivalTime, burstTime):
    n = len(processes)
    waitingTime = [0] * n
    completed = [False] * n
    currentTime = 0
    completedCount = 0

    while completedCount < n:
        # Find the next process to execute
        idx = -1
        minBurst = float('inf')
        for i in range(n):
            if not completed[i] and arrivalTime[i] <= currentTime and burstTime[i] < minBurst:
                minBurst = burstTime[i]
                idx = i

        if idx == -1:  # No process is ready, advance time
            currentTime += 1
            continue

        # Execute the selected process
        waitingTime[idx] = currentTime - arrivalTime[idx]
        currentTime += burstTime[idx]
        completed[idx] = True
        completedCount += 1

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
    zipped = sorted(zip(arrivalTime, burstTime, processes), key=lambda x: (x[1],x[0]))
    # arrivalTime, burstTime, processes = zip(*zipped)
    sorted_arrivalTime = [item[0] for item in zipped]
    sorted_burstTime = [item[1] for item in zipped]
    sorted_processes = [item[2] for item in zipped]

    waitingTime = sjf_non_preemptive(sorted_processes, sorted_arrivalTime, sorted_burstTime)
    turnaroundTime = calculateTurnaroundTime(sorted_burstTime, waitingTime)

    avgWaitingTime = sum(waitingTime) / len(sorted_processes)
    avgTurnaroundTime = sum(turnaroundTime) / len(sorted_processes)

    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(f"{processes[i]}\t\t{arrivalTime[i]}\t\t{burstTime[i]}\t\t{waitingTime[i]}\t\t{turnaroundTime[i]}")

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
    
    print("\nFCFS Scheduling Algorithm with User Input:")
    calculateAverageTimes(processes, arrivalTime, burstTime)

# Main function
if __name__ == "__main__":
    acceptDisplay()
