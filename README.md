#Number of genes per sample

This script will analyze how many times pairs of identifiers (usually genes) appear together. The input consists of any number of lines of any number of genes together on each line:

```
gene1, gene2, gene3
gene1, gene3, gene4, gene5
```

A sample input file is included.

The output is of the format:

```
gene1, gene2, 1
gene1, gene3, 2
gene1, gene4, 1
...
```

This format is useful for creating weighted graphs in which the edges are weighted by how often the nodes occur together in experiments. 