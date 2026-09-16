## EXERCISE: py_hidenp  (Level 3)
  ────────────────────────────────────────────────────────
  Assignment name  : py_hidenp
  Expected files   : py_hidenp.py
  Allowed functions: None
  --------------------------------------------------------------------------------
  
  Write a function that checks if the string 'small' is a subsequence
  of 'big'. A subsequence means all characters of 'small' appear in 'big'
  in the same order, but not necessarily consecutively.
  Function is case-sensitive.
  
  Your function must be declared as follows:
  
      def hidenp(small: str, big: str) -> bool:
  
  Examples:
      hidenp("abc", "a1b2c3")              -> True
      hidenp("ace", "abcde")               -> True
      hidenp("aec", "abcde")               -> False
      hidenp("", "abc")                    -> True
      hidenp("abc", "ab")                  -> False
      hidenp("aaaa", "aaa")                -> False
      hidenp("sing","subsequence testing") -> True
  ────────────────────────────────────────────────────────

  📁  Work dir : exam_workspace
  📝  Create   : py_hidenp.py

## EXERCISE: py_number_base_converter  (Level 3)
  ────────────────────────────────────────────────────────
  Assignment name  : py_number_base_converter
  Expected files   : py_number_base_converter.py
  Allowed functions: None
  --------------------------------------------------------------------------------
  
  Write a function that converts a number from one base to another.
  Support bases from 2 to 36 inclusive.
  Use digits 0-9 and letters A-Z for values 10-35.
  Return "ERROR" for invalid inputs.
  
  Your function must be declared as follows:
  
      def number_base_converter(number: str, from_base: int, to_base: int) -> str:
  
  Examples:
      number_base_converter("1010", 2, 10)  -> "10"
      number_base_converter("FF", 16, 10)   -> "255"
      number_base_converter("255", 10, 16)  -> "FF"
      number_base_converter("123", 10, 2)   -> "1111011"
      number_base_converter("Z", 36, 10)    -> "35"
      number_base_converter("35", 10, 36)   -> "Z"
      number_base_converter("123", 1, 10)   -> "ERROR"
      number_base_converter("G", 16, 10)    -> "ERROR"
  ────────────────────────────────────────────────────────

  📁  Work dir : exam_workspace
  📝  Create   : py_number_base_converter.py


## EXERCISE: py_pattern_tracker  (Level 3)
────────────────────────────────────────────────────────
  Assignment name  : py_pattern_tracker
  Expected files   : py_pattern_tracker.py
  Allowed functions: None
  --------------------------------------------------------------------------------
  
  Write a function that counts the number of valid consecutive digit pairs
  in a string. A valid pair consists of two adjacent digits where the second
  digit is exactly one greater than the first.
  A 9 followed by a 0 is NOT a valid pair.
  
  Your function must be declared as follows:
  
      def pattern_tracker(text: str) -> int:
  
  Examples:
      pattern_tracker("123")        -> 2
      pattern_tracker("12a34")      -> 2
      pattern_tracker("987654321")  -> 0
      pattern_tracker("01234567")   -> 7
      pattern_tracker("abc")        -> 0
      pattern_tracker("1a2b3c4")    -> 0
      pattern_tracker("112233")     -> 2
────────────────────────────────────────────────────────

  📁  Work dir : exam_workspace
  📝  Create   : py_pattern_tracker.py


## EXERCISE: py_inter  (Level 3)
  ────────────────────────────────────────────────────────
  Assignment name  : py_inter
  Expected files   : py_inter.py
  Allowed functions: None
  --------------------------------------------------------------------------------

  Write a function that returns a string with the characters that appear
  in both strings, without repetitions. Characters are added in the order
  they appear in the first string.

  Your function must be declared as follows:

      def inter(s1: str, s2: str) -> str:

  Examples:
      inter("hello", "world")   -> "lo"
      inter("banana", "band")   -> "ban"
      inter("abcabc", "bc")     -> "bc"
      inter("abc", "xyz")       -> ""
      inter("", "abc")          -> ""
  ────────────────────────────────────────────────────────

  📁  Work dir : exam_workspace
  📝  Create   : py_inter.py


