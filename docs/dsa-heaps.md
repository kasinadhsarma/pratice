# 🏔️ DSA — Heap Data Structure

**Location:** [`dsa/heaps/`](../dsa/heaps/)

A **Heap** is a complete binary tree stored as an implicit array. The heap property guarantees $\mathcal{O}(1)$ access to the maximum (or minimum) element and $\mathcal{O}(\log N)$ insertion and removal.

---

## Max-Heap — `maxheap.py`

Every parent node is **greater than or equal to** its children. The **root always holds the maximum element**.

### Array Representation

For a node at index `i` (0-based):

```
parent(i)      = (i - 1) // 2
left_child(i)  = 2*i + 1
right_child(i) = 2*i + 2
```

**Heap Property:** `heap[parent] >= heap[child]` for every node.

---

### Operations

#### `insert(val)` — $\mathcal{O}(\log N)$
1. Append `val` to the end of the array.
2. **Bubble up (sift up):** while `val > parent`, swap them.
   Restores heap property from bottom to top.

#### `extract_max()` — $\mathcal{O}(\log N)$
1. Root (`index 0`) is the maximum.
2. Replace root with the last element; remove last element.
3. **Bubble down (heapify-down):** swap root with its largest child until heap property is restored.

#### `get_max()` — $\mathcal{O}(1)$
1. Return `heap[0]`.

#### Build heap from $N$ elements — $\mathcal{O}(N)$
Using repeated `heapify-down` from index `n//2 - 1` to `0`.

---

### Complexity Summary

| Operation | Time | Space |
|:---|:---|:---|
| `insert` | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| `extract_max` | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ |
| `get_max` | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| Build heap | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

---

### Applications

- **Priority Queues** — always process the highest-priority item first
- **Heap Sort** — $\mathcal{O}(N \log N)$ in-place sort
- **K Largest / K Smallest Elements**
- **Graph Algorithms** — Prim's MST, Dijkstra's Shortest Path

---

## How to Run

```bash
python ./dsa/heaps/maxheap.py
# Input: space-separated integers to build the heap
# Output: max element, extracted max, remaining heap
```

---

## Min-Heap (Coming Soon)

A **min-heap** follows the same structure but the root holds the **minimum element**. Useful for:
- Dijkstra's shortest path
- Merge K sorted lists
- Finding the median of a data stream
