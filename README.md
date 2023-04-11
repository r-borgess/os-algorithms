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
A simple FIFO modification that avoids the problem of throwing away a heavily used page by inspecting older page's reference bit. Assume that the R bit of all
pages is reset every 4 (four) memory references.

### Optimal
Each page should be labeled with the number of instructions that will be executed before that page is referenced
for the first time. The optimal algorithm says that the page with the highest label must be removed.

### Working Set
Finds a page that is not in the working set and remove it. For this, the system keeps: 
  - The moment of the last use for each pag
  - The current virtual time (incremented with each memory reference) 
  - A threshold that must always be half the number of frames of memory page plus 1 (one). Ex: If n=4, then threshold = 4 / 2 + 1 = 3.
Consider that the R bit of all pages is reset every 4 (four) memory references.

### Input
Atxt file containing a series of integers, one per line, with the first one indicating the number of frames available in RAM and the rest indicating the sequence of memory references. It must be passed from the standard input.
Example:
```
4
1
2
3
4
1
2
5
1
2
3
4
5
```
### Output
The output is composed of lines containing the abbreviation of each of the three algorithms and the number of page faults obtained using each one of them.
Example:
```
SC 7
OTM 6
CT 8
```
## Disk Arm Scheduling

### *First Come, First Served* (FCFS)

The requests are served in the order they arrive.

When a disk request is received, it is added to the end of the request queue. The disk arm then starts serving the requests from the front of the queue, moving towards the end of the disk. Once the arm reaches the last request in the queue, it reverses direction and starts serving requests in the opposite direction, moving towards the beginning of the disk.

### *Shortest Seek Time First* (SSTF)

In this algorithm, the disk arm moves to the request that is closest to its current position, rather than simply serving requests in the order they arrive.

When a disk request is received, the algorithm looks for the request in the queue that has the shortest distance from the current position of the disk arm. This request is then moved to the front of the queue, and the disk arm serves it first.

Once this request has been served, the algorithm repeats the process of finding the next closest request and moving it to the front of the queue. This continues until all the requests in the queue have been served.

### Elevator

In this algorithm, the disk arm moves in a single direction, servicing requests in that direction until it reaches the end of the disk. Once it reaches the end, the disk arm reverses direction and starts servicing requests in the other direction, again until it reaches the end of the disk.

When a disk request is received, it is added to the request queue in its appropriate position based on the current direction of the disk arm. If the arm is currently moving towards the higher sector numbers, the request is added to the queue in its proper place in ascending order. If the arm is moving towards the lower sector numbers, the request is added to the queue in descending order.

### Input
A txt file containing a series of integers, one per line, with the first one indicating the number of the last cylinder on the disk (cylinders vary
from 0 to this number), the second one indicating the cylinder on which the r/w head is initially positioned and the following numbers indicating the sequence of access requests.
Example:
```
199
53
98
183
37
122
14
124
65
67
```

### Output
The output is composed of lines containing the abbreviation of each of the three algorithms and the total number of cylinders traversed by the reading head to
serve all disk access requests.
Example:
```
FCFS 640
SSTF 236
ELEVATOR 299
```
## Execution

`python <filename.py> < <filename.txt>`
