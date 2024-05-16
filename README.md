# Uber Code Interview

## Escape Route Algorithm


This repository implements an algorithm to find an escape route in a grid-like map, simulating a scenario where you're lost on land ("1") surrounded by water ("0") and need to find a continuous path from the top to the bottom.

## Example

The provided code includes a sample map (defined as matriz) and asserts the expected results for three scenarios:

A map with a valid escape route.
A map with no starting point (all cells in the first row are water).
A map with no valid escape route (land cells are disconnected).

Here is a case with a path:

```
m = 
[  [0, 1, 1, 0],
   [0, 0, 1, 1],
   [1, 1, 1, 1],
   [1, 0, 0, 0] ]
```

```
Path Sample:
   [        1 ]
   [        1 ]
   [ 1  1   1 ]
   [ 1        ]
```

