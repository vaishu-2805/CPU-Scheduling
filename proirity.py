def priority_non_preemptive(processes, arrivalTime, burstTime, priority):
    n = len(processes)
    completed = [False] * n
    waitingTime = [0] * n
    turnaroundTime = [0] * n
    currentTime = 0
    completedCount = 0
    execution_log = []

    while completedCount < n:
        idx = -1
        highestPriority = float('inf')

        for i in range(n):
            if not completed[i] and arrivalTime[i] <= currentTime:
                if priority[i] < highestPriority or (priority[i] == highestPriority and arrivalTime[i] < arrivalTime[idx]):
                    highestPriority = priority[i]
                    idx = i

        if idx == -1:
            currentTime += 1
            continue

        start_time = currentTime
        currentTime += burstTime[idx]
        end_time = currentTime
        execution_log.append((processes[idx], start_time, end_time))

        waitingTime[idx] = start_time - arrivalTime[idx]
        turnaroundTime[idx] = waitingTime[idx] + burstTime[idx]
        completed[idx] = True
        completedCount += 1

    return waitingTime, turnaroundTime, execution_log

def printGanttChart(execution_log):
    print("\nGantt Chart:")
    print(" ", end="")
    for p, st, et in execution_log:
        print("------", end="")
    print("\n|", end="")
    for p, st, et in execution_log:
        print(f"  {p}  |", end="")
    print("\n ", end="")
    for p, st, et in execution_log:
        print("------", end="")
    print()
    for p, st, et in execution_log:
        print(f"{st:<6}", end="")
    print(f"{execution_log[-1][2]}")

def calculateAverageTimes(processes, arrivalTime, burstTime, priority):
    waitingTime, turnaroundTime, execution_log = priority_non_preemptive(processes, arrivalTime, burstTime, priority)

    print("\nProcess\tArrival Time\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(f"{processes[i]}\t\t{arrivalTime[i]}\t\t{burstTime[i]}\t\t{priority[i]}\t\t{waitingTime[i]}\t\t{turnaroundTime[i]}")

    printGanttChart(execution_log)

    avgWT = sum(waitingTime) / len(processes)
    avgTAT = sum(turnaroundTime) / len(processes)

    print(f"\nAverage Waiting Time: {avgWT:.2f}")
    print(f"Average Turnaround Time: {avgTAT:.2f}")

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

    print("\nPriority Scheduling (Non-Preemptive) Algorithm with User Input:")
    calculateAverageTimes(processes, arrivalTime, burstTime, priority)

if __name__ == "__main__":
    acceptDisplay()
