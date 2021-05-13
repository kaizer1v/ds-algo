# Algorithms

A computational procedure to solve some problem

When you are given a problem initially, you first write an algorithm i.e. how you are going to solve it (using mathemetics) and then convert it into computer code.

Program                 <-> Algorithm
Programming Language    <-> Psuedo code / Structured English
Computer                <-> Model of computation
                            (what operations should do + how much they cost)


## How Python Works

* `L.append(x)` - happens in constant time using a concept of table doubling
* `L = L1 + L2` - is the same as
  ```
  L = []          # O(1)
  for x in L1:
    L.append(x)   # O(1) * len(L1)
  for x in L2:
    L.append(x)   # O(1) * len(L2)
  ```
  So total time = O(L1 + L2 + 1)
* `len(L)`      - takes constant time, because python maintains a counter inside
* `L.sort()`    - takes `n log(n)`, uses comparison sort
* When you write a program, use a dictionary