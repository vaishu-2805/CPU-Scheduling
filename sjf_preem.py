def sjf_preemptive(processes, arrivalTime, burstTime):
    n = len(processes)
    remainingTime = burstTime[:]  # Copy burst time for remaining execution
    waitingTime = [0] * n
    completed = [False] * n
    currentTime = 0
    completedCount = 0
    execution_log = []  # To track (process, start_time, end_time)
    lastProcess = None
    startTime = [-1] * n

    while completedCount < n:
        # Find the process with the shortest remaining time
        idx = -1
        minRemaining = float('inf')
        for i in range(n):
            if not completed[i] and arrivalTime[i] <= currentTime and remainingTime[i] < minRemaining:
                minRemaining = remainingTime[i]
                idx = i

        if idx == -1:
            currentTime += 1
            continue

        # Start tracking execution
        if lastProcess != idx:
            execution_log.append([processes[idx], currentTime, currentTime + 1])
        else:
            execution_log[-1][2] += 1  # Extend end time

        if startTime[idx] == -1:
            startTime[idx] = currentTime

        remainingTime[idx] -= 1
        currentTime += 1
        lastProcess = idx

        if remainingTime[idx] == 0:
            completed[idx] = True
            completedCount += 1
            waitingTime[idx] = (currentTime - arrivalTime[idx] - burstTime[idx])

    return waitingTime, execution_log

def calculateTurnaroundTime(burstTime, waitingTime):
    return [burstTime[i] + waitingTime[i] for i in range(len(burstTime))]

def printGanttChart(execution_log):
    print("\nGantt Chart:")
    print(" ", end="")
    for p, st, et in execution_log:
        print("----", end="")
    print("\n|", end="")
    for p, st, et in execution_log:
        print(f" {p} |", end="")
    print("\n ", end="")
    for p, st, et in execution_log:
        print("----", end="")
    print()
    for p, st, et in execution_log:
        print(f"{st:<4}", end="")
    print(f"{execution_log[-1][2]}")

def calculateAverageTimes(processes, arrivalTime, burstTime):
    waitingTime, execution_log = sjf_preemptive(processes, arrivalTime, burstTime)
    turnaroundTime = calculateTurnaroundTime(burstTime, waitingTime)

    avgWaitingTime = sum(waitingTime) / len(processes)
    avgTurnaroundTime = sum(turnaroundTime) / len(processes)

    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(f"{processes[i]}\t\t{arrivalTime[i]}\t\t{burstTime[i]}\t\t{waitingTime[i]}\t\t{turnaroundTime[i]}")

    printGanttChart(execution_log)

    print(f"\nAverage Waiting Time: {avgWaitingTime:.2f}")
    print(f"Average Turnaround Time: {avgTurnaroundTime:.2f}")

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

    print("\nSJF Preemptive (SRTF) Scheduling Algorithm with User Input:")
    calculateAverageTimes(processes, arrivalTime, burstTime)

# Main function
if __name__ == "__main__":
    acceptDisplay()
