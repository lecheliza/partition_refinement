# partition_refinement

Partition refinement, also known as color refinement, is an algorithm used to detect potentially isomorphic graphs by marking two vertices with the same color if they have similar neighbourhoods. Two graphs might be isomorphic if they share the same set of colored vertices.

This repository contains source code for partition refinement algorithm and graph class provided by University of Twente that was edited to fit my needs better.

## Usage
Specify the file in the `main.py` and then run the script in the command line as follows:
```bash
python main.py
```
For example, running the algorithm with file `colorref_smallexample_4_16.grl` returns
```bash
--- 0.008895635604858398 seconds ---
Possibly isomorphic graphs: [0, 1] 
Possibly isomorphic graphs: [2, 3] discrete
--- 0.006983757019042969 seconds ---
```
