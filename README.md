# partition_refinement

Partition refinement, also known as color refinement, is an algorithm used to detect potentially isomorphic graphs by marking two vertices in the separate graphs with the same color if and only if they have similar neighbourhoods. Two graphs might be isomorphic if they share the same set of colored vertices. The coloring is discrete if every color appears only on one vertex in a given graph.

This repository contains source code for partition refinement algorithm and graph class provided by University of Twente that was edited to fit my needs better.

## Usage
Make sure that the file is present in `test_files` directory. Then, specify the file name as an argument as follows:
```bash
python main.py "filename"
```
For example, running the algorithm with file `colorref_smallexample_4_16.grl` returns
```bash
> python main.py "colorref_smallexample_4_16.grl"
Possibly isomorphic graphs: [0, 1]
Possibly isomorphic graphs: [2, 3] discrete
--- 0.004658937454223633 seconds ---
```
