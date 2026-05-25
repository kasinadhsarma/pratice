# 📊 DSA — Sorting Algorithms

**Location:** [`dsa/sorting/`](../dsa/sorting/)

Five classic comparison-based sorting algorithms, each implemented as a standalone OOP class with detailed docstring explanations.

---

## Algorithms

### 🫧 Bubble Sort — `bubblesort.py`

Repeatedly compares adjacent elements and swaps them if out of order. After each pass the largest unsorted element "bubbles" to its final position.

| | |
|:---|:---|
| **Best Case** | $\mathcal{O}(N)$ — already sorted (early exit on no swaps) |
| **Average / Worst** | $\mathcal{O}(N^2)$ |
| **Space** | $\mathcal{O}(1)$ — in-place |
| **Stable** | ✅ Yes |

---

### 📌 Insertion Sort — `insertionsort.py`

Builds the sorted array one item at a time by inserting each new element into its correct position among the already-sorted elements.

| | |
|:---|:---|
| **Best Case** | $\mathcal{O}(N)$ — already sorted |
| **Average / Worst** | $\mathcal{O}(N^2)$ |
| **Space** | $\mathcal{O}(1)$ — in-place |
| **Stable** | ✅ Yes |

---

### 🔍 Selection Sort — `selectionsort.py`

Repeatedly finds the minimum element from the unsorted portion and swaps it to the front.

| | |
|:---|:---|
| **Best / Average / Worst** | $\mathcal{O}(N^2)$ — always scans remaining elements |
| **Space** | $\mathcal{O}(1)$ — in-place |
| **Stable** | ❌ No (swaps can disrupt equal-element order) |

---

### ⚡ Merge Sort — `mergesort.py`

Divide-and-conquer: recursively splits the array in half, sorts each half, then merges the sorted halves.

| | |
|:---|:---|
| **Best / Average / Worst** | $\mathcal{O}(N \log N)$ |
| **Space** | $\mathcal{O}(N)$ — auxiliary arrays during merge |
| **Stable** | ✅ Yes |

**Recurrence:** $T(N) = 2T(N/2) + \mathcal{O}(N)$ → $\mathcal{O}(N \log N)$ by Master Theorem.

---

### 🏹 Quick Sort — `quicksort.py`

Divide-and-conquer: picks a pivot, partitions the array so smaller elements go left and larger go right, then recursively sorts each partition.

| | |
|:---|:---|
| **Best / Average** | $\mathcal{O}(N \log N)$ |
| **Worst Case** | $\mathcal{O}(N^2)$ — sorted input with bad pivot choice |
| **Space** | $\mathcal{O}(\log N)$ — recursion stack |
| **Stable** | ❌ No |

---

## Comparison Summary

| Algorithm | Best | Average | Worst | Space | Stable |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bubble Sort | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | ✅ |
| Insertion Sort | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | ✅ |
| Selection Sort | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | ❌ |
| Merge Sort | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ | ✅ |
| Quick Sort | $O(N \log N)$ | $O(N \log N)$ | $O(N^2)$ | $O(\log N)$ | ❌ |

---

## How to Run

```bash
python ./dsa/sorting/bubblesort.py
python ./dsa/sorting/mergesort.py
python ./dsa/sorting/quicksort.py
```
