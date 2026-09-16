## EXERCISE: py_string_sculptor  (Level 5)
  ────────────────────────────────────────────────────────
  Assignment name  : py_string_sculptor
  Expected files   : py_string_sculptor.py
  Allowed functions: None
  --------------------------------------------------------------------------------
  
  Write a function that transforms a string by alternating the case of
  alphabetic characters only.
  Non-alphabetic characters remain unchanged and are NOT counted in the
  alternation index.
  The first alphabetic character should be lowercase, the second uppercase, etc.
  Spaces reset the alternation (next alpha after a space is lowercase again).
  
  Your function must be declared as follows:
  
      def string_sculptor(text: str) -> str:
  
  Examples:
      string_sculptor("hello")        -> "hElLo"
      string_sculptor("Hello World")  -> "hElLo wOrLd"
      string_sculptor("abc123def")    -> "aBc123DeF"
      string_sculptor("Python3.9!")   -> "pYtHoN3.9!"
      string_sculptor("")             -> ""
  ────────────────────────────────────────────────────────

  📁  Work dir : exam_workspace
  📝  Create   : py_string_sculptor.py


## EXERCISE: py_twist_sequence  (Level 5)
  ────────────────────────────────────────────────────────
  Assignment name  : py_twist_sequence
  Expected files   : py_twist_sequence.py
  Allowed functions: None
  --------------------------------------------------------------------------------

  Write a function that rotates an array to the right by k positions.
  Rotating right by k means the last k elements move to the front.

  Your function must be declared as follows:

      def twist_sequence(arr: list[int], k: int) -> list[int]:

  Examples:
      twist_sequence([1,2,3,4,5], 2)  -> [4,5,1,2,3]
      twist_sequence([1,2,3], 1)      -> [3,1,2]
      twist_sequence([1,2,3,4], 0)    -> [1,2,3,4]
      twist_sequence([1,2,3], 5)      -> [2,3,1]
      twist_sequence([], 3)           -> []
  ────────────────────────────────────────────────────────

  📁  Work dir : exam_workspace
  📝  Create   : py_twist_sequence.
