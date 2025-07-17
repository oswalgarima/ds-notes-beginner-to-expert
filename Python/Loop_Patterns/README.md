
# Pattern Printing Practice — Loops in Python

📚 Topic: Loops & Patterns
📅 Date Studied: 17th July 2025

---

This repository contains solutions to classic loop-based pattern questions in Python — the kind asked in beginner coding rounds and interviews. All patterns were practiced over 2 days using nested `for` loops and basic conditional logic.

---

## 🧠 What’s Inside?

| 🔢 Pattern Type                         | 🖥️ Output Preview                 | 🧾 Python Logic Description |
|----------------------------------------|----------------------------------|-----------------------------|
| 1. Left-Aligned Increasing Numbers     | 1<br>12<br>123<br>1234<br>12345  | `for i in range(1, 6)` + print 1 to i |
| 2. Right-Aligned Triangle              | &nbsp;&nbsp;&nbsp;&nbsp;1<br>&nbsp;&nbsp;&nbsp;12<br>&nbsp;&nbsp;123<br>&nbsp;1234<br>12345 | Use `range(5 - i)` spaces before numbers |
| 3. Reverse Triangle Numbers            | 54321<br>5432<br>543<br>54<br>5  | Reverse loop from 5 to i |
| 4. Star Patterns (Left & Pyramid)      | *****<br>****<br>***<br>**<br>*  | Simple nested loops with decreasing range |
| 5. Number Pyramid                      | 1<br>121<br>12321<br>1234321     | Loop forward then reverse |
| 6. Alternating Binary                  | 10101<br>01010                   | `if (i+j) % 2 == 0` logic |
| 7. Repeated Digits / Letters           | 1<br>22<br>333<br>4444<br>55555  | Print i, i times |
| 8. Prime Number Triangle               | 2<br>3 5<br>7 11 13              | Loop to generate prime numbers |
| 9. Skipped Number Series               | 2 4 6<br>1 3 5 7<br>...          | Use step in range |
| 10. Asterisk Centered Triangle         | &nbsp;&nbsp;&nbsp;*<br>&nbsp;&nbsp;***<br>&nbsp;***** | Use spaces + stars with logic `2*i-1` |

---

## ✅ Solved Patterns

---

### 🔢 Pattern 1: Repeating Same Row

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

```python
for i in range(4):
    for j in range(1, 6):
        print(j, end=' ')
    print()


⸻

🔢 Pattern 2: Decreasing Columns

1 2 3 4 5  
1 2 3 4  
1 2 3  
1 2  
1

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()


⸻

🔢 Pattern 3: Increasing Left-Aligned Triangle

1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()


⸻

🔢 Pattern 4: Right-Aligned Increasing Numbers

        1  
      1 2  
    1 2 3  
  1 2 3 4  
1 2 3 4 5

for i in range(1, 6):
    print('  ' * (5 - i), end='')
    for j in range(1, i+1):
        print(j, end=' ')
    print()


⸻

🔢 Pattern 5: Reverse Decreasing

5 4 3 2 1  
5 4 3 2  
5 4 3  
5 4  
5

for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end=' ')
    print()


⸻

🔢 Pattern 6: Diagonal Triangle Numbers

1  
2 3  
4 5 6  
7 8 9 10

count = 1
for i in range(1, 5):
    for j in range(i):
        print(count, end=' ')
        count += 1
    print()


⸻

🔢 Pattern 7: Star Pyramid

*  
**  
***  
****  
*****

for i in range(1, 6):
    print('*' * i)


⸻

🔢 Pattern 8: 0-1 Alternate

10101  
01010  
10101  
01010  
10101

for i in range(5):
    for j in range(5):
        print((i + j) % 2, end='')
    print()


⸻

🔢 Pattern 9: Row = Column Value

1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5

for i in range(1, 6):
    print((str(i) + ' ') * i)


⸻

🔢 Pattern 10: All 1s

1 1 1 1 1

print('1 ' * 5)


⸻

🔢 Pattern 11: Multiples (Prime Numbers)

1  
2 3  
5 7 11  
13 17 19 23  
29 31 37 41 47

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

count = 0
num = 2
for i in range(1, 6):
    for j in range(i):
        while not is_prime(num):
            num += 1
        print(num, end=' ')
        num += 1
    print()

---

## 💬 One-Line Summary

> “Mastering patterns trains your logic muscle — one loop at a time!”

---

⸻

🔁 Flash Prompts
	1.	How do you align a triangle to the right using spaces?
	2.	What’s the difference between print('*' * i) vs nested for loops?
	3.	How can you detect prime numbers in a loop?
	4.	When do you use while inside for?

⸻

🧠 Happy Looping!
