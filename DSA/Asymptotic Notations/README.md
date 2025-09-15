⸻

# 📘 Day 3: Asymptotic Notations – Big O, Big Omega & Big Theta

---

## 📌 What You Will Learn Today

### 🔍 Asymptotic Notations

These are ways to describe how algorithms behave when input size gets really big.

- **Big O (O‑notation):** Upper bound — worst case  
  Think: “How slow can it get?”  
- **Big Omega (Ω‑notation):** Lower bound — best case  
  Think: “What’s the fastest it can be?”  
- **Big Theta (Θ‑notation):** Both bounds — best & worst combined  
  Think: “How tight is the guess?”

---

### 🧒 Child‑Level Analogies

| Notation           | What It Means in Simple Words                                | Real‑Life Example                      |
|---------------------|--------------------------------------------------------------|-----------------------------------------|
| Big O (O)           | “It won’t be slower than this”                               | Worst traffic time to get home         |
| Big Omega (Ω)       | “It won’t be faster than this”                                | Best possible traffic, no red lights    |
| Big Theta (Θ)       | “Usually somewhere around here — between slow and fast”       | Your usual commute between best/worst   |

---

### 🔗 Relationships

- If an algorithm is Θ(f(n)), it means it's both O(f(n)) **and** Ω(f(n)).
- Big O is used most often, especially for worst‑case analysis.

---

### 🐍 & 💻 Examples (Python and C++)

**Python Example: Checking in a list**  

```python
def contains(lst, x):
    for item in lst:
        if item == x:
            return True   # Best case: finds immediately — Ω(1)
    return False          # Worst case: checks all — O(n)
```

C++ Example: Similarly

```cpp
bool contains(vector<int>& lst, int x) {
    for(int i = 0; i < lst.size(); i++) {
        if(lst[i] == x) {
            return true;   // Best case: early exit Ω(1)
        }
    }
    return false;          // Worst case: full loop, O(n)
}
```

⸻

📊 Summary Table

Concept	What It Describes	Why It’s Helpful
Big O	Maximum time / worst case performance	Prepares us for the slowest scenario
Big Omega	Minimum time / best case performance	Shows the fastest possible case
Big Theta	Both bounds — tight bound	Gives “typical range” of performance


⸻

💬 One‑Line Summary

“Big O is how slow it could get, Big Omega is how fast, and Big Theta says it usually lives somewhere in between.”

⸻

🔁 Flash Revision Prompts
-	1.	What’s the difference between Big O and Big Omega?
-	2.	Why do we care about worst‑case (Big O) more than best‑case in many scenarios?
-	3.	Give an example of an algorithm with Θ(n).
-	4.	How would you argue that an algorithm is not Θ(f(n))?

⸻

✅ Citation

📚 Based on: Asymptotic Notations: Big O, Big Omega and Big Theta Explained by CodeWithHarry
📺 YouTube Playlist: DSA in C/C++ – CodeWithHarry
🧠 All credit for video content goes to the original creator.

⸻
