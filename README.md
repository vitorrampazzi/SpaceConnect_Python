# SpaceConnect

A Python terminal application that simulates satellite monitoring and telemetry to demonstrate data structures and algorithms.

Developed for the **Global Solution 2026 — First Semester** academic project.

## Demonstration flow

1. Load satellite records from `satelites_data.csv`.
2. Build and display a catalog using a singly linked list.
3. Queue and process sample telemetry packets.
4. Record commands in a stack and undo the latest command.
5. Sort satellites by ID with Quick Sort.
6. Find a satellite in the sorted catalog with binary search.

Satellite records, telemetry packets, and commands are demonstration data. Pauses between steps make the simulation easier to follow; no live telemetry service is connected.

## Data structures and algorithms

| Implementation | Role |
| --- | --- |
| Singly linked list | Satellite catalog |
| FIFO queue | Sequential telemetry processing |
| LIFO stack | Command history and undo |
| Quick Sort | Ordering satellites by ID |
| Binary search | Looking up a satellite in the sorted list |

## Run locally

**Requirement:** Python 3. The application uses only the standard-library `csv` and `time` modules.

```bash
git clone https://github.com/vitorrampazzi/SpaceConnect_Python.git
cd SpaceConnect_Python
python main.py
```

On Windows, `py main.py` can also be used.

Run the command from the repository root so the program can find the CSV file. No `pip` installation is required.

## Repository structure

| File | Purpose |
| --- | --- |
| `main.py` | Data loading and demonstration sequence |
| `estruturas.py` | Linked list, queue, and stack |
| `algoritmos.py` | Quick Sort and binary search |
| `satelites_data.csv` | Demonstration satellite dataset |

## Team

- Vitor Rampazzi Franco — RM: 562270
- Daniel Brito — RM: 566236
- Gustavo Borsato — RM: 564621
