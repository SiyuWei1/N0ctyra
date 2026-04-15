# M05-IC-PRACTS-02: Functions + Function Theory — Answers

---

## Act-#1: Well-Defined Functions?

**Domain:** X = {finite non-empty bit strings}，**Codomain:** Y = {0, 1, 2, 3, ...}

**a) f: X → Y, f(s) = number of ones in s**
**Well-defined. ✓**
Every finite bit string has a definite count of ones (0 to n). One input → one output, always in Y.

**b) g: X → Y, g(s) = first bit of s**
**Well-defined. ✓**
Every non-empty string has a unique first bit (0 or 1), and both 0 and 1 are in Y.

**c) h: X → Y, h(s) = position of the leftmost zero in s**
**NOT well-defined. ✗**
If s = "1" or "111", there is no zero, so h(s) is undefined. Not every input maps to an output.

**d) j: X → X, j(s) = string obtained by appending 0 or 1 to s**
**NOT well-defined. ✗**
"0 or 1" means there are two possible outputs for each input — a function must map each input to exactly one output.

**e) k: Y → X, k(n) = string of n ones**
**NOT well-defined. ✗**
k(0) = "" (empty string), but X contains only *non-empty* strings. So k(0) ∉ X.

---

## Act-#2: One-to-One and Onto

**a) ord: C → {0,...,127}**
- **One-to-one: Yes** — different characters have different ASCII codes.
- **Onto: Yes** — every integer 0–127 is the ASCII code of exactly one character.
- ord is a **bijection**.

**b) chr: {0,...,127} → C**
- **One-to-one: Yes** — different numbers produce different characters.
- **Onto: Yes** — every character c equals chr(ord(c)), so every character is in the range.
- chr is a **bijection** (and chr = ord⁻¹).

**c) f: R → R, f(x) = 2x + 1**
- **One-to-one: Yes** — if f(x₁) = f(x₂), then 2x₁+1 = 2x₂+1, so x₁ = x₂.
- **Onto: Yes** — for any y ∈ R, x = (y−1)/2 gives f(x) = y.
- f is a **bijection**.

**d) f from Act-#1(a): f: X → Y, f(s) = number of ones in s**
- **One-to-one: No** — f("0") = 0 and f("00") = 0, two different inputs map to the same output.
- **Onto: Yes** — for any n ≥ 0, the string of n ones (or "0" for n=0) maps to n.

**e) Φ: X → X, Φ(s) = s with "0" appended**
- **One-to-one: Yes** — if s₁+"0" = s₂+"0", then s₁ = s₂.
- **Onto: No** — the string "1" is not in the range (every output ends in "0", "1" ends in "1").

---

## Act-#3a: All Functions from A = {1,2} to B = {1,2,3}

Total: 3² = **9 functions**

| f(1) | f(2) |
|------|------|
| 1    | 1    |
| 1    | 2    |
| 1    | 3    |
| 2    | 1    |
| 2    | 2    |
| 2    | 3    |
| 3    | 1    |
| 3    | 2    |
| 3    | 3    |

---

## Act-#3b: f: R → R, f(x) = x² − 1

**(a) f at −10?**
f(−10) = (−10)² − 1 = 100 − 1 = **99**

**(b) f(−10)?**
Same: **99**

**(c) What argument gives value 80?**
x² − 1 = 80 → x² = 81 → x = **±9**

**(d) f(80)?**
f(80) = 80² − 1 = 6400 − 1 = **6399**

**(e) Image of 4?**
f(4) = 16 − 1 = **15**

**(f) Pre-image of 15?**
x² − 1 = 15 → x² = 16 → x = **±4**

**(g) All pre-images of 12?**
x² − 1 = 12 → x² = 13 → x = **±√13**

**(h) All pre-images of −1?**
x² − 1 = −1 → x² = 0 → x = 0
Pre-image = **{0}**

---

## Act-#4: Composition of Functions

**X** = all finite non-empty character strings, **N** = non-negative integers
- f: X → N, f(s) = length of s
- g: X → X, g(s) = s with 'a' appended

**a) f ∘ f**
f(s) ∈ N, but f requires input from X. Since N ≠ X, f cannot take f(s) as input.
**Does NOT exist.**

**b) f ∘ g** (i.e., f(g(s)))
g(s) ∈ X ✓, so f(g(s)) is valid.
(f ∘ g)(s) = f(s + 'a') = |s| + 1
**Exists. f ∘ g : X → N, (f ∘ g)(s) = |s| + 1**

**c) g ∘ f** (i.e., g(f(s)))
f(s) ∈ N, but g requires input from X. Since N ≠ X, g cannot take f(s) as input.
**Does NOT exist.**

**d) g ∘ g** (i.e., g(g(s)))
g(s) ∈ X ✓, so g(g(s)) is valid.
(g ∘ g)(s) = g(s + 'a') = s + 'aa'
**Exists. g ∘ g : X → X, appends "aa" to s.**

---

## Act-#2 (Second): upr and lwr

**a) Evaluate:**
- upr('Barbara Hill') = **'BARBARA HILL'**
- (lwr ∘ upr)('Barbara Hill') = lwr('BARBARA HILL') = **'barbara hill'**

**b) Are upr and lwr inverses?**
**No.**
For upr and lwr to be inverses, we need (lwr ∘ upr)(s) = s for all s ∈ S.
But (lwr ∘ upr)('Barbara Hill') = 'barbara hill' ≠ 'Barbara Hill'.
The composition "flattens" mixed-case strings to all lowercase, so information (original capitalization) is lost — upr is not one-to-one, and therefore invertible only on restricted domains.

---

## Act-#3 (Second): f and g on Words

**X = {1,...,20}, Y = non-null strings up to 20 chars**
- f: X → Y, f(x) = English word for x (e.g., f(1)='one', f(7)='seven', f(20)='twenty')
- g: Y → X, g(s) = number of characters in s

**a) Is f one-to-one? Onto? Does f⁻¹ exist?**
- **One-to-one: Yes** — 'one', 'two', ..., 'twenty' are all distinct strings.
- **Onto: No** — Y contains strings like 'hello', 'xyz', 'cat', etc. that are not English number words.
- **f⁻¹ exists: No** (as a function from Y to X) — since f is not onto, not every element of Y has a pre-image. f⁻¹ would only exist if restricted to Range(f) = {'one','two',...,'twenty'}.

**b) Evaluate compositions:**

**(g ∘ f)(7)**
= g(f(7))
= g('seven')
= number of characters in 'seven'
= **5**

**(f ∘ g)('seven')**
= f(g('seven'))
= f(5)
= English word for 5
= **'five'**
