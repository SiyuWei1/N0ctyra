import Data.Char (isDigit, isLower, isUpper)

-- ============================================================
-- Act #1 (5 pts) - Types of the following values
-- ============================================================
-- a. ['a','b','c']           :: [Char]
-- b. ('a','b','c')           :: (Char, Char, Char)
-- c. [(False,'0'),(True,'1')]:: [(Bool, Char)]
-- d. [isDigit,isLower,isUpper] :: [Char -> Bool]


-- ============================================================
-- Act #2 (10 pts) - List comprehension results
-- ============================================================
-- a. [x | x <- [1,2,3], False]
--    Result: []
--    Reason: The guard is always False, so no element passes.

-- b. [not (x && y) | x <- [False, True], y <- [False, True]]
--    Result: [True, True, True, False]
--    Explanation:
--      x=False, y=False => not (False && False) = not False = True
--      x=False, y=True  => not (False && True)  = not False = True
--      x=True,  y=False => not (True && False)  = not False = True
--      x=True,  y=True  => not (True && True)   = not True  = False

-- c. [x || y | x <- [False, True], y <- [False, True], x /= y]
--    Result: [True, True]
--    Explanation:
--      x=False, y=False => x /= y is False, skipped
--      x=False, y=True  => x /= y is True,  False || True  = True
--      x=True,  y=False => x /= y is True,  True  || False = True
--      x=True,  y=True  => x /= y is False, skipped

-- d. [[x,y,z] | x <- [1..50], y <- [1..50], z <- [1..50], x*x + y*y == z*z]
--    Result: all Pythagorean triples where x, y, z are in [1..50]
--    e.g. [3,4,5], [4,3,5], [5,12,13], [6,8,10], ...


-- ============================================================
-- Act #3 (5 pts) - Returns True if the character is 'a'
-- ============================================================
isA :: Char -> Bool
isA 'a' = True
isA _   = False


-- ============================================================
-- Act #4 (5 pts) - Returns True if the string is "hello"
-- ============================================================
isHello :: String -> Bool
isHello ('h':'e':'l':'l':'o':[]) = True
isHello _                        = False


-- ============================================================
-- Act #5 (5 pts) - Removes a leading space if it exists
-- ============================================================
removeLeadingSpace :: String -> String
removeLeadingSpace (' ':xs) = xs
removeLeadingSpace xs       = xs


-- ============================================================
-- Act #6 (5 pts) - Returns elements greater than n
-- ============================================================
greaterThan :: [Int] -> Int -> [Int]
greaterThan xs n = [x | x <- xs, x > n]


-- ============================================================
-- Act #7 (8 pts) - Returns indexes where n appears in the list
-- ============================================================
f :: [Int] -> Int -> [Int]
f xs n = [i | (x, i) <- zip xs [0..], x == n]


-- ============================================================
-- Act #8 (7 pts) - Converts a list of Int to Bool (0=False, 1=True)
-- ============================================================
convert :: [Int] -> [Bool]
convert []     = []
convert (0:xs) = False : convert xs
convert (1:xs) = True  : convert xs
convert (_:xs) = convert xs
