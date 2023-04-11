# os-algorithms
Implementation of some Process Scheduling, Page Replacement and Disk Arm Scheduling algorithms.

## Process Scheduling
### Dynamic priorities
  - Each process is assigned the same initial scheduling priority which changes over time.
  - If the process is not in the running state, the scheduler periodically increases its priority.
  - The more the process uses the CPU, the more the scheduler reduces its priority.
  - Priorities change every instant of time. 
  - The scheduler always selects the process with the highest priority among those in the ready state
  - Processes with the same priority must follow the order of arrival in the queue.
  - The scheduler **MUST** force preemption of the running process every time that there is a higher priority process.
### Lottery
  - A value between 0 and n-1 is assigned to each process, where n is the number of processes.
  - A number is drawn.
  - The chosen process is put in execution for a quantum.
  - At the end of each quantum, the process is repeated.
### Circular Alternation (Round Robin with quantum=2)
  - All processes are stored in a circular queue.
  - Each process is assigned a unit of time called a quantum.
  **NOTE: Consider the queue sorted by process ID with the same time of arrival.**
### Input
A txt file with a series of integer pairs separated by blank space indicating the time of arrival of the process and the duration of each process. It must be given from the standard input.
Example:
```
0 2
0 3
1 2
1 4
```
### Output
Each line presents the abbreviation of the algorithm and the average values for return time, response time, and wait time, exactly
in that order, separated by a blank space.
Output example:
```
PRI 7.50 1.00 4.75
LOT 7.00 2.50 4.25
RR 6.50 2.50 3.75
```

## Page Replacement

### Second Chance

### Optimal

### Working Set

### Input

### Output

## Disk Arm Scheduling

### *First Come, First Served* (FCFS)

### *Shortest Seek Time First* (SSTF)

### Elevator

### Input

### Output

## Execution
