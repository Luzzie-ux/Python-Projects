## EXERCISE: py_cryptic_sorter  (Level 1)
  ────────────────────────────────────────────────────────
  Assignment name  : py_cryptic_sorter
  Expected files   : py_cryptic_sorter.py
  Allowed functions: None
  --------------------------------------------------------------------------------
  
  Write a function that sorts a list of strings according to multiple criteria:
  1. Primary sort: By string length (shortest first)
  2. Secondary sort: ASCII order, except letters are compared case-insensitively
     (for strings of same length)
  3. Tertiary sort: By number of vowels (ascending, for same length and lexically equal)
  4. Equal strings will appear in the same order as in the input list.
  
  Your function must be declared as follows:
  
      def cryptic_sorter(strings: list[str]) -> list[str]:
  
  The function should return the sorted list.
  
  Your function must handle:
    - Empty strings and empty lists
    - Mixed case strings (treat as lowercase for sorting)
    - Special characters (ignore for vowel counting)
  
  Examples:
      cryptic_sorter(["apple","cat","banana","dog","elephant"])
          -> ["cat","dog","apple","banana","elephant"]
      cryptic_sorter(["aaa","bbb","AAA","BBB"])
          -> ["aaa", "AAA", "bbb", "BBB"]
      cryptic_sorter(["hello","world","hi","test"])
          -> ["hi","test","hello","world"]
      cryptic_sorter([])       -> []
      cryptic_sorter([""])     -> [""]
  ────────────────────────────────────────────────────────

  📁  Work dir : exam_workspace
  📝  Create   : py_cryptic_sorter.py


## EXERCISE: py_bracket_validator  (Level 1)
  ────────────────────────────────────────────────────────
  Assignment name  : py_bracket_validator
  Expected files   : py_bracket_validator.py
  Allowed functions: None
  --------------------------------------------------------------------------------
  
  Write a function that checks if the brackets in a string are valid.
  
  A string is valid if every opening bracket has a matching closing bracket
  in the correct order.
  
  Allowed brackets: (), [], {}
  
  Your function must be declared as follows:
  
      def bracket_validator(s: str) -> bool:
  
  Examples:
      bracket_validator("()")           -> True
      bracket_validator("()[]{}")       -> True
      bracket_validator("(]")           -> False
      bracket_validator("([)]")         -> False
      bracket_validator("{[]}")         -> True
      bracket_validator("hello(world)") -> True
      bracket_validator("((())")        -> False
      bracket_validator("")             -> True
  ────────────────────────────────────────────────────────

  📁  Work dir : exam_workspace
  📝  Create   : py_bracket_validator.py

