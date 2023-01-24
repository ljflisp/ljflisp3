#echo "Hello World!"
import strutils
proc rot13(c: char): char = 
  case toLowerAscii(c)
  of 'a'..'m': chr(ord(c)+13)
  of 'n'..'z': chr(ord(c)-13)
  else:        c
  
#for c in "I love my dad.":
  # stdout.write  rot13(c)
#stdout.write "\n"
proc  factorial(x: int): int = 
  result = 1
  for i in 2..x:
    result *= i
echo factorial(5)