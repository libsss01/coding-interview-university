# Big-O & Time Complexity Notes

## 1. Big-O Definition

Big-O is a notation used to describe how the running time or memory usage of an algorithm grows when the input size grows.

Big-O does not tell us exactly how fast a program is.  
It describes the growth rate of an algorithm.

---

## 2. Complexity

Complexity usually refers to two things:

- Time complexity: how the number of operations grows.
- Space complexity: how memory usage grows.

When we just say "complexity", we usually refer to time complexity.

---

## 3. Input Size

`n` represents the size of the input.

Examples:

- If we have a list of 100 items, then n = 100.
- If we have 1,000 flashcards, then n = 1,000.
- If we have 10,000 users, then n = 10,000.

---

## 4. Common Time Complexities

- O(1): constant cost / constant time
- O(log n): the problem is divided at each step / logarithmic time
- O(n): one pass over the input / linear time
- O(n log n): logarithmic levels with linear work at each level / linearithmic time
- O(n²): nested loops over the same input / quadratic time

Order from fastest growth to slowest growth:

O(1) < O(log n) < O(n) < O(n log n) < O(n²)

---

## 5. Big-O, Omega and Theta

- O(...) describes an upper bound.
- Ω(...) describes a lower bound.
- Θ(...) describes a tight bound.
