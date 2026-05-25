# 🧠 DSA Basics — Logic Levels

**Location:** [`dsa/basics/logic/`](../dsa/basics/logic/)

Logic exercises structured into **three progressive levels**, covering conditional branching, digit extraction, number theory, and mathematical series. All scripts are implemented with **OOP Classes** for clean encapsulation.

> **Note:** Level 1 and Level 2 algorithms operate in $\mathcal{O}(1)$ constant space — no extra data structures are stored.

---

## 🟢 Level 1 — Basic Conditions & Branching

**Location:** [`dsa/basics/logic/level1/`](../dsa/basics/logic/level1/)

Focuses on simple `if/else` checks and basic modulo arithmetic.

- **Time Complexity:** $\mathcal{O}(1)$ — constant time
- **Space Complexity:** $\mathcal{O}(1)$

| File | Description | Key Logic |
| :--- | :--- | :--- |
| `even_odd.py` | Checks if a number is even or odd | `num % 2 == 0` |
| `leapyear.py` | Determines if a year is a leap year | Divisibility by 4, 100, 400 |

---

## 🟡 Level 2 — Digit Extraction & Manipulation

**Location:** [`dsa/basics/logic/level2/`](../dsa/basics/logic/level2/)

Introduces extracting digits using `num % 10` and reducing the number with `num // 10` in a loop.

- **Time Complexity:** $\mathcal{O}(\log_{10}(N))$ — iterations = number of digits in $N$
- **Space Complexity:** $\mathcal{O}(1)$

| File | Description | Key Concept |
| :--- | :--- | :--- |
| `sum_of_digits.py` | Iteratively sums every digit of an integer | `digit = num % 10` |
| `reversenumber.py` | Reverses the order of digits (`123` → `321`) | Build reversed number digit-by-digit |
| `palindrome_number.py` | Checks if a number reads the same forwards and backwards | Compare original vs reversed |
| `armstrong_number.py` | Sum of cubes of digits equals the number itself | $1^3 + 5^3 + 3^3 = 153$ |
| `strong_number.py` | Sum of factorials of digits equals the number itself | $1! + 4! + 5! = 145$ |

---

## 🔴 Level 3 — Series, Factors & Divisor Search

**Location:** [`dsa/basics/logic/level3/`](../dsa/basics/logic/level3/)

Covers iterative series generation, divisor search, and loop optimization (e.g., searching only up to $\sqrt{N}$).

| File | Description | Time Complexity |
| :--- | :--- | :--- |
| `prime_check.py` | Checks if a number is prime | $\mathcal{O}(\sqrt{N})$ |
| `perfectnumber.py` | Sum of proper divisors equals the number ($1+2+3=6$) | $\mathcal{O}(\sqrt{N})$ |
| `fabonacci.py` | Generates Fibonacci sequence up to $N$ terms | $\mathcal{O}(N)$ |
| `factorial.py` | Computes $N!$ — product of all positive integers up to $N$ | $\mathcal{O}(N)$ |
| `gcd.py` | Greatest Common Divisor via Euclid's algorithm | $\mathcal{O}(\log(\min(a,b)))$ |
| `direction_tracker.py` | Tracks position after a series of directional moves | $\mathcal{O}(N)$ |

---

## How to Run

```bash
# Level 1
python ./dsa/basics/logic/level1/even_odd.py
python ./dsa/basics/logic/level1/leapyear.py

# Level 2
python ./dsa/basics/logic/level2/armstrong_number.py
python ./dsa/basics/logic/level2/strong_number.py

# Level 3
python ./dsa/basics/logic/level3/prime_check.py
python ./dsa/basics/logic/level3/gcd.py
```
