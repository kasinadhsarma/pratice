# 💡 DSA — Dynamic Programming (DP)

**Location:** [`dsa/dp/`](../dsa/dp/)

**Dynamic Programming** solves problems by breaking them into overlapping subproblems, storing the results of each subproblem to avoid redundant computation. This is the core difference from plain recursion.

> **Key Insight:** DP = Recursion + Memoization (top-down) or Tabulation (bottom-up).

---

## Core DP Concepts

| Concept | Description |
|:---|:---|
| **Optimal Substructure** | The optimal solution to the whole problem is built from optimal solutions to its subproblems |
| **Overlapping Subproblems** | The same subproblems are solved multiple times — DP caches their answers |
| **Memoization (Top-Down)** | Recursive solution + cache (dictionary/array) to store computed results |
| **Tabulation (Bottom-Up)** | Iteratively fill a table starting from base cases up to the final answer |

---

## Problems

---

### 🎒 0/1 Knapsack — `knapsack_01.py`

**Technique:** Dynamic Programming — bottom-up tabulation  
**Type:** 0/1 Choice (take an item or leave it — no fractions)

#### Problem Statement
Given $N$ items each with weight $w[i]$ and value $v[i]$, and a knapsack of capacity $W$:  
**Find the maximum total value you can carry.**

#### Recurrence
```
dp[i][w] = maximum value using first i items with capacity w

Base case:  dp[0][w] = 0   for all w   (no items → no value)

Recurrence:
  if w[i] > w :  dp[i][w] = dp[i-1][w]                     ← item too heavy, skip
  else         :  dp[i][w] = max(
                      dp[i-1][w],                            ← skip item i
                      dp[i-1][w - w[i]] + v[i]              ← take item i
                  )

Answer: dp[N][W]
```

#### Steps
1. Build a 2D table `dp` of size `(n+1) × (W+1)` initialised to `0`.
2. For each item `i` (1 to n), for each capacity `w` (0 to W): apply recurrence.
3. `dp[n][W]` is the answer.

#### Complexity
| | |
|:---|:---|
| **Time** | $\mathcal{O}(N \times W)$ — filling the DP table |
| **Space** | $\mathcal{O}(N \times W)$ — DP table *(reducible to $\mathcal{O}(W)$ with 1D rolling array)* |

#### Why not Greedy?
Greedy (pick by value/weight ratio) **fails** for 0/1 Knapsack because you cannot take fractions — taking the "best ratio" item may leave a gap in the bag that a combination of smaller items could fill better.

---

### 🎒 Fractional Knapsack — `knapsack_fractional.py`

**Technique:** Greedy — sort by value-to-weight ratio  
**Type:** Fractional Choice (can take any fraction of an item)

#### Problem Statement
Same as 0/1, but you **can take fractions of items**.

#### Greedy Criterion
```
ratio[i] = v[i] / w[i]    (value per unit weight)

Sort items by ratio descending.

For each item (sorted):
    take = min(w[i], remaining_capacity)
    profit += take × (v[i] / w[i])
    remaining_capacity -= take
```

#### Why Greedy is Optimal Here
The **exchange argument** proves it: swapping any fraction of a lower-ratio item for a fraction of the highest-ratio item never decreases total profit. This argument **does not hold** for 0/1 Knapsack because items can't be split.

#### Complexity
| | |
|:---|:---|
| **Time** | $\mathcal{O}(N \log N)$ — dominated by sorting |
| **Space** | $\mathcal{O}(N)$ — item list with ratios |

---

## 0/1 vs Fractional Knapsack — Comparison

| | 0/1 Knapsack | Fractional Knapsack |
|:---|:---|:---|
| **Item Choice** | Whole item only (0 or 1) | Any fraction allowed |
| **Technique** | Dynamic Programming | Greedy |
| **Time** | $O(N \times W)$ | $O(N \log N)$ |
| **Space** | $O(N \times W)$ | $O(N)$ |
| **Optimal Greedy?** | ❌ No — DP required | ✅ Yes |

---

## Classic DP Problems Roadmap

The following problems extend naturally from the Knapsack foundation:

| Problem | Technique | Difficulty |
|:---|:---|:---|
| 0/1 Knapsack | 2D DP Table | ⭐⭐ |
| Fractional Knapsack | Greedy + Sort | ⭐ |
| Longest Common Subsequence (LCS) | 2D DP Table | ⭐⭐ |
| Longest Increasing Subsequence (LIS) | DP + Binary Search | ⭐⭐⭐ |
| Coin Change (min coins) | 1D DP | ⭐⭐ |
| Matrix Chain Multiplication | Interval DP | ⭐⭐⭐ |
| Edit Distance | 2D DP Table | ⭐⭐⭐ |
| Rod Cutting | Unbounded Knapsack DP | ⭐⭐ |

---

## How to Run

```bash
# 0/1 Knapsack
python ./dsa/dp/knapsack_01.py
# Enter: number of items, weights, values, capacity

# Fractional Knapsack
python ./dsa/dp/knapsack_fractional.py
# Enter: number of items, weights, values, capacity
```

### Example (0/1 Knapsack)
```
enter number of items: 3
enter weights separated by space: 2 3 4
enter values separated by space: 3 4 5
enter knapsack capacity: 5
maximum value: 7
```

### Example (Fractional Knapsack)
```
enter number of items: 3
enter weights separated by space: 10 20 30
enter values separated by space: 60 100 120
enter knapsack capacity: 50
maximum value: 240.0
```
