: GREET S" Hello World!" ;
GREET TYPE
: COUNTDOWN ( N --)
  BEGIN CR DUP . 1 - DUP 0 =      UNTIL DROP ;
5 COUNTDOWN
: NESTED ( n m --) CR
  0 DO DUP ( n m --)
   0 DO CR J .   I .
   LOOP
  LOOP
DROP ;
2 3 NESTED 


4 8 15 16 23 42 - + - + * .
1 8 16 15 24 57 - + - + * .
1 1 1 3 2 2 - + - + * .
1 2 3 * - .
1 2 3 - * .
3 2 1 - * .
4 3 2 1 - * - .
bye