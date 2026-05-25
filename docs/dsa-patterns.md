# 🔲 DSA Basics — Pattern Printing

**Location:** [`dsa/basics/`](../dsa/basics/)

Programs that teach nested loop bounds, horizontal/vertical coordination, and space offset calculations by printing visual triangle patterns using stars or numbers.

> **Complexity (all patterns):**
> - Time: $\mathcal{O}(N^2)$ — quadratic due to nested loops
> - Space: $\mathcal{O}(1)$ — output is streamed directly, no arrays stored

---

## 🌟 Star Patterns

**Location:** [`dsa/basics/stars/`](../dsa/basics/stars/)

| File | Shape | Technique |
| :--- | :--- | :--- |
| `rightangletraingle.py` | Left-aligned right triangle | Outer loop = rows, inner loop = stars |
| `leftangletriangle.py` | Right-aligned right triangle | Leading space offsets |
| `middletraingle.py` | Centered star pyramid | Space prefix = `N - i`, stars = `2*i - 1` |

---

## 🔢 Number Patterns

**Location:** [`dsa/basics/numbers/`](../dsa/basics/numbers/)

| File | Shape | Technique |
| :--- | :--- | :--- |
| `rightangletraingle.py` | Left-aligned incrementing number rows | Print `j` for `j in range(1, i+1)` |
| `leftangletriangle.py` | Right-aligned incrementing number rows | Leading space offsets + numbers |
| `middletriangle.py` | Centered number pyramid | Space prefix + incrementing numbers |

---

## How to Run

```bash
python ./dsa/basics/stars/middletraingle.py
python ./dsa/basics/numbers/middletriangle.py
```
