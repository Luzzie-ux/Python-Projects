## EXERCISE: py_anagram  (Level 4)
────────────────────────────────────────────────────────
  Assignment name  : py_anagram
  Expected files   : py_anagram.py
  Allowed functions: None
  --------------------------------------------------------------------------------
  
  Write a function that checks if two strings are anagrams.
  They must contain exactly the same letters with the same quantity,
  ignoring case and spaces.
  
  Your function must be declared as follows:
  
      def anagram(s1: str, s2: str) -> bool:
  
  Examples:
      anagram("listen", "silent")             -> True
      anagram("Triangle", "Integral")         -> True
      anagram("Dormitory", "Dirty Room")      -> True
      anagram("hello", "world")               -> False
      anagram("", "")                         -> True
      anagram("abc", "abcc")                  -> False
────────────────────────────────────────────────────────

  📁  Work dir : exam_workspace
  📝  Create   : py_anagram.py


## EXERCISE: py_shadow_merge  (Level 4)
────────────────────────────────────────────────────────
  Assignment name  : py_shadow_merge
  Expected files   : py_shadow_merge.py
  Allowed functions: None
  --------------------------------------------------------------------------------
  
  Write a function that merges two sorted lists into one sorted list.
  
  Your function must be declared as follows:
  
      def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
  
  Examples:
      shadow_merge([1,3,5], [2,4,6])    -> [1,2,3,4,5,6]
      shadow_merge([1,2,3], [4,5,6])    -> [1,2,3,4,5,6]
      shadow_merge([1], [2,3,4])        -> [1,2,3,4]
      shadow_merge([], [1,2,3])         -> [1,2,3]
      shadow_merge([1,1,2], [1,3,3])    -> [1,1,1,2,3,3]
────────────────────────────────────────────────────────

  📁  Work dir : exam_workspace
  📝  Create   : py_shadow_merge.py


## EXERCISE: py_string_permutation_checker  (Level 4)
  ────────────────────────────────────────────────────────
  Assignment name  : py_string_permutation_checker
  Expected files   : py_string_permutation_checker.py
  Allowed functions: None
  --------------------------------------------------------------------------------

  Write a function that determines if two strings are permutations of each other.
  Case sensitive. Whitespace and punctuation count as regular characters.
  Empty strings are permutations of each other.

  Your function must be declared as follows:

      def string_permutation_checker(s1: str, s2: str) -> bool:

  Examples:
      string_permutation_checker("abc", "bca")              -> True
      string_permutation_checker("abc", "def")              -> False
      string_permutation_checker("listen", "silent")        -> True
      string_permutation_checker("hello", "bello")          -> False
      string_permutation_checker("", "")                    -> True
      string_permutation_checker("a", "")                   -> False
      string_permutation_checker("Abc", "abc")              -> False
      string_permutation_checker("a gentleman","elegant man")-> True
  ────────────────────────────────────────────────────────

  📁  Work dir : exam_workspace
  📝  Create   : py_string_permutation_checker.py

