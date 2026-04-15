# M05- IC-PRACTS-01 - FP with Haskell Coding: Tutorial

The content items in this tutorial summarize some key Haskell types, functions and syntax, some of which we already covered in the Haskell Lecture notes. Browse through these examples using the `ghci REPL` prompt to check and reflect on the outputs, then complete the Graded Activities that follow. Please enter Your Answers directly in the Answer Textbox provided.

---

## Basic Types in Haskell

Haskell has a number of basic types, including:
- `Bool` - Logical values
- `Char` - Single characters
- `String` - Strings of characters
- `Int` - Fixed-precision integers
- `Integer` - Arbitrary-precision integers

---

## List Types

```haskell
[False,True,False] :: [Bool]
['a','b','c','d'] :: [Char]
```

In general:
A list is sequence of values of the same type:
`[T]` is the type of lists with elements of type T. List may be used to model sets and other computer-based collection types.

---

## Pairs & Tuple Types

We can pair things together like so:

```haskell
p :: (Int, Char)
p = (3, 'x')

("dog","cat") :: (String,String)
(True, 5) :: (Bool,Int)
('a',"b") :: (Char,String)
("bat",(3.14,False)) :: (String,(Double,Bool))
```

Notice that the (x,y) notation is used both for the type of a pair and a pair value.

The elements of a pair can be extracted again with pattern matching:

```haskell
sumPair :: (Int,Int) -> Int
sumPair (x,y) = x + y
```

Haskell also has triples, quadruples, … but you don't really need to use them. Signature of some library functions on pairs:

```haskell
fst :: (a,b) -> a
snd :: (a,b) -> b
```

## Function Types in Haskell

A function is a mapping from values of one type (the domain of the function) to values of another type (the co-domain):

`T1 → T2` is the type of functions that map arguments of type T1 to results of type T2.

```haskell
not :: Bool → Bool
isDigit :: Char → Bool
not False :: Bool  -- a function application produces a value
False && True :: Bool
```

We use the notation `e :: T` to mean that evaluating the expression e will produce a value of type T.

---

Under the ghci you may test the type of a data item or function using: `:t <data-item-or-function-value-or-name>`. For example:

```haskell
ghci> :t 4                                          -- What's the type of value 4
4 :: Num a => a                              -- anything of type a that implements the Num behavior or interface

ghci> :t True                -- what's the type of value True?
True :: Bool                 -- type Bool

ghci> :t not                 -- What's the type of the not function?
not :: Bool -> Bool          -- not maps values from domain Bool to co-domain Bool
```

---

## Act #1. What are the types of the following values? (5 points)

a. `['a','b','c']`
b. `('a','b','c')`
c. `[(False,'0'),(True,'1')]`
d. `[isDigit,isLower,isUpper]` -- in ghci use: `import Data.Char` -- to enable the 3 functions on characters

## Act #2. Work out the values of the following list comprehensions; then check your results by evaluating them in ghci (10 points):

a. `[x | x <- [1,2,3], False]`
b. `[not (x && y) | x <- [False, True], y <- [False, True]]`
c. `[x || y | x <- [False, True], y <- [False, True], x /= y]`
d. `[[x,y,z] | x <- [1..50], y <- [1..50], z <- [1..50], x ** 2 + y ** 2 == z ** 2]`

---

## Haskell Built-in Functions on Lists in the Standard Prelude

```haskell
length [1,2,3,4]
product [1,2,3,4]
take 3 [1,2,3,4,5]
```

## Defining Functions in Haskell

Defining a function is the same as defining a variable (You may type following in a file, say test.hs):

```haskell
double x = x + x
quadruple x = double (double x)

factorial n = product [1..n]
average ns = sum ns `div` length ns
```

Then invoke as: `ghci test.hs` -- or you can first start ghci then use the `:l <file-name>` to load file

## Function Application -- Calling the functions you already define

```haskell
> quadruple 10               -- call quadruple with 10 as input -- reductions as follows
  ==> double (double 10)
  ==> double (10 + 10)
  ==> double 20
  ==> 20 + 20 ==> 40

> take (double 2) [1..6]     -- function application with composition, reduction follows
  ==> take (2 + 2) [1..6]
  ==> take 4 [1..6]
  ==> [1,2,3,4]
```

---

## Boolean logic in Haskell

As you would expect, Boolean values can be combined with `(&&)` (logical and), `(||)` (logical or), and `not`. For example,

```haskell
ex11 = True && False
ex12 = not (False || True)
```

Things can be compared for equality with `(==)` and `(/=)`, or compared for order using `(<)`, `(>)`, `(<=)`, and `(>=)`.

```haskell
ex13 = ('a' == 'a')
ex14 = (16 /= 3)
ex15 = (5 > 3) && ('p' <= 'q')
ex16 = "Haskell" > "C++"
```

Haskell also has if-expressions: `if b then t else f` is an expression which evaluates to `t` if the Boolean expression `b` evaluates to True, and `f` if `b` evaluates to False. Notice that if-expressions are very different than if-statements. For example, with an if-statement, the else part can be optional; an omitted else clause means "if the test evaluates to False then do nothing". With an if-expression, on the other hand, the else part is required, since the if-expression must result in some value.

Idiomatic Haskell does not use if expressions very much, often using pattern-matching or guards instead (see the next section).

---

## Defining basic functions

We can write functions on integers by cases.

```haskell
-- Compute the sum of the integers from 1 to n.
sumtorial :: Integer -> Integer
sumtorial 0 = 0
sumtorial n = n + sumtorial (n-1)
```

Note the syntax for the type of a function: `sumtorial :: Integer -> Integer` says that sumtorial is a function which takes an Integer as input and yields another Integer as output.

Each clause is checked in order from top to bottom, and the first matching clause is chosen. For example, `sumtorial 0` evaluates to 0, since the first clause is matched. `sumtorial 3` does not match the first clause (3 is not 0), so the second clause is tried. A variable like n matches anything, so the second clause matches and `sumtorial 3` evaluates to `3 + sumtorial (3-1)` (which can then be evaluated further).

Choices can also be made based on arbitrary Boolean expressions using guards. For example:

```haskell
hailstone :: Integer -> Integer
hailstone n
  | n `mod` 2 == 0 = n `div` 2
  | otherwise      = 3*n + 1
```

Any number of guards can be associated with each clause of a function definition, each of which is a Boolean expression. If the clause's patterns match, the guards are evaluated in order from top to bottom, and the first one which evaluates to True is chosen. If none of the guards evaluate to True, matching continues with the next clause.

For example, suppose we evaluate `hailstone 3`. First, 3 is matched against n, which succeeds (since a variable matches anything). Next, `n \`mod\` 2 == 0` is evaluated; it is False since n = 3 does not result in a remainder of 0 when divided by 2. `otherwise` is just a convenient synonym for True, so the second guard is chosen, and the result of `hailstone 3` is thus `3*3 + 1 = 10`.

As a more complex (but more contrived) example:

```haskell
foo :: Integer -> Integer
foo 0 = 16
foo 1
  | "Haskell" > "C++" = 3
  | otherwise         = 4
foo n
  | n < 0            = 0
  | n `mod` 17 == 2  = -43
  | otherwise        = n + 3
```

What is `foo (-3)`? `foo 0`? `foo 1`? `foo 36`? `foo 38`?

As a final note about Boolean expressions and guards, suppose we wanted to abstract out the test of evenness used in defining hailstone. A first attempt is shown below:

```haskell
isEven :: Integer -> Bool
isEven n
  | n `mod` 2 == 0 = True
  | otherwise      = False
```

This works, but it is much too complicated. Can you see why?

## Using functions, and multiple arguments

To apply a function to some arguments, just list the arguments after the function, separated by spaces, like this:

```haskell
f :: Int -> Int -> Int -> Int
f x y z = x + y + z
ex17 = f 3 17 8
```

The above example applies the function f to the three arguments 3, 17, and 8. Note also the syntax for the type of a function with multiple arguments, like `Arg1Type -> Arg2Type -> ... -> ResultType`. This might seem strange to you (and it should!). Why all the arrows? Wouldn't it make more sense for the type of f to be something like `Int Int Int -> Int`? Actually, the syntax is no accident: it is the way it is for a very deep and beautiful reason, which we'll learn about in a few weeks; for now you just have to take my word for it!

Note that function application has higher precedence than any infix operators. So it would be incorrect to write

```haskell
f 3 n+1 7
```

if you intend to pass `n+1` as the second argument to f, because this parses as

```haskell
(f 3 n) + (1 7).
```

Instead, one must write

```haskell
f 3 (n+1) 7.
```

Some Built-in Haskell functions and their types are:

```haskell
sqrt :: Double -> Double
max :: Integer -> Integer -> Integer
not :: Bool -> Bool
toUpper :: Char -> Char

(+) :: Integer -> Integer -> Integer
(&&) :: Bool -> Bool -> Bool
```

---

## More About Lists

Lists are one of the most basic data types in Haskell.

```haskell
nums, range, range2 :: [Integer]
nums   = [1,2,3,19]
range  = [1..100]
range2 = [2,4..100]
```

Haskell (like Python) also has list comprehensions.

Strings are just lists of characters. That is, `String` is just an abbreviation for `[Char]`, and string literal syntax (text surrounded by double quotes) is just an abbreviation for a list of Char literals.

```haskell
-- hello1 and hello2 are exactly the same.
hello1 :: [Char]
hello1 = ['h', 'e', 'l', 'l', 'o']

hello2 :: String
hello2 = "hello"

helloSame = hello1 == hello2
```

This means that all the standard library functions for processing lists can also be used to process Strings.

## Constructing lists

The simplest possible list is the empty list:

```haskell
emptyList = []
```

Other lists are built up from the empty list using the cons operator, `(:)`. Cons takes an element and a list, and produces a new list with the element prepended to the front.

```haskell
ex18 = 1 : []
ex19 = 3 : (1 : [])
ex20 = 2 : 3 : 4 : []
ex21 = [2,3,4] == 2 : 3 : 4 : []
```

We can see that `[2,3,4]` notation is just convenient shorthand for `2 : 3 : 4 : []`. Note also that these are really singly linked lists, NOT arrays.

```haskell
-- Generate the sequence of hailstone iterations from a starting number.
hailstoneSeq :: Integer -> [Integer]
hailstoneSeq 1 = [1]
hailstoneSeq n = n : hailstoneSeq (hailstone n)
```

We stop the hailstone sequence when we reach 1. The hailstone sequence for a general n consists of n itself, followed by the hailstone sequence for `hailstone n`, that is, the number obtained by applying the hailstone transformation once to n.

## Functions on lists

We can write functions on lists using pattern matching.

```haskell
-- Compute the length of a list of Integers.
intListLength :: [Integer] -> Integer
intListLength []     = 0
intListLength (x:xs) = 1 + intListLength xs
```

The first clause says that the length of an empty list is 0. The second clause says that if the input list looks like `(x:xs)`, that is, a first element x consed onto a remaining list xs, then the length is one more than the length of xs.

Since we don't use x at all we could also replace it by an underscore: `intListLength (_:xs) = 1 + intListLength xs`.

We can also use nested patterns:

```haskell
sumEveryTwo :: [Integer] -> [Integer]
sumEveryTwo []         = []     -- Do nothing to the empty list
sumEveryTwo (x:[])     = [x]    -- Do nothing to lists with a single element
sumEveryTwo (x:(y:zs)) = (x + y) : sumEveryTwo zs
```

Note how the last clause matches a list starting with x and followed by… a list starting with y and followed by the list zs. We don't actually need the extra parentheses, so `sumEveryTwo (x:y:zs) = ...` would be equivalent.

## Common Functions on Lists

```haskell
length :: [a] -> Int
length [2,8,1] => 3
length [] => 0
length "hello" => 5
length [1..n] => n
```

### The `!!` (index) Operator

The `(!!)` operator lets you access a list element by its index. Indices start from 0.

```haskell
(!!) :: [a] -> Int -> a
[1,2,3] !! 0 => 1
"abcde" !! 2 => 'c'
```

### The `take` Function

This function takes the first n elements from a list:

```haskell
take :: Int -> [a] -> [a]
take 2 [1,2,3] => [1,2]
take 0 [1,2,3] => []
take 4 [1,2,3] => [1,2,3]
```

### The `drop` Function

The drop function drops the first n elements from a list; it removes exactly the same elements that take would return:

```haskell
drop :: Int -> [a] -> [a]
drop 2 [1,2,3] => [3]
drop 0 [1,2,3] => [1,2,3]
drop 4 [1,2,3] => []
```

### The `++` (append) Operator

Two lists can be joined together using the append (also called concatenation) `(++)` operation. All of the elements in the resulting list must have the same type, so the two lists must also have the same type.

```haskell
(++) :: [a] -> [a] -> [a]
[1,2] ++ [3,4,5] => [1,2,3,4,5]
[] ++ "abc" => "abc"
```

### The `map` Function

Often, we want to apply a function to each element in a list. For example, we may have a string of lower case letters and want them to be upper case letters. To do this, we use `map`, which takes a function of one argument and a list. It applies the function to each element of the list.

```haskell
map :: (a -> b) -> [a] -> [b]
map toUpper "the cat and dog" => "THE CAT AND DOG"
map (* 10) [1,2,3] => [10,20,30]
```

The map function is often used in functional programming to solve problems where you would use a for loop in an imperative language. When you need to perform some computation on all the elements of a list xs, define a function f to do the computation, and write `map f xs`.

---

## Additional Practice Coding Activities

The following functions (signature and definition shown), which are defined in the standard Haskell libraries, can be used to return the first element of a list (the head), or everything except the first element (the tail):

```haskell
head :: [a] -> a
head (x:xs) = x

tail :: [a] -> [a]
tail (x:xs) = xs
```

**Act #3.** Write a function that takes a character and returns True if the character is 'a' and False otherwise. (5 points)

**Act #4.** Write a function that takes a string and returns True if the string is "hello" and False otherwise. This can be done by specifying each element of the string in the list pattern (e.g. `'h':'i':[]`). (5 points)

**Act #5.** Write a function that takes a string and removes a leading space if it exists. (5 points)

**Act #6.** Using a list comprehension, write a function that takes a list of Int values and an Int value n and returns those elements in the list that are greater than n. (5 points)

**Act #7.** Write a function: `f :: [Int] -> Int -> [Int]` that takes a list of Int values and an Int and returns a list of indexes at which that Int appears. (8 points)

**Act #8.** Suppose a program has read in a list of numbers of type Int. Each number is intended to represent a Boolean value, where 0 means False, 1 means True, and any other number constitutes invalid input. Write a function `convert :: [Int] -> [Bool]` that converts a list of numbers to the corresponding Booleans. (7 points)
