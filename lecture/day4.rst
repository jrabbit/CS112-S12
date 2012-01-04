==============================
If and While
==============================
Day 4 [2.M] (2/6)
------------------------------


Flow Control
-------------
 * Most of programming has to do with "flow control".
 * the flow of a program is how we know which instructions to run


Loops
-------------
 * do something while something else is true
 * explain while loops with countdown
 * `see example 1 <d4ex1.py>`_
    * forget to subtract 1 from c
    * point out it is infinite, terminate with Ctrl-C
    * add decrement
    * run again
    * point out import
    * point out whitespacing now?
 * show real infinite while loop
    * ``while True: print "you can't catch me"``
    * ``running=True: while running: print "You can't catch me!"``
 * modify ex1 with second loop at top to prevent c from being 0
 * Game of Nibs (homework?) 
   `see example 2 <d4ex2.py>`_
 * Random colors
   `see example 3 <d4ex3.py>`_

If
---------------
 * if statements let you create forks in your code
 * "if it is monday, then I am sad"
 * just like whiles, if's take conditionals

Logic
-------------
 * ==, <, >, <=, >=, !=
   * height < 60
   * a == b
   * s != ""
 * and, or, not
   * between, ``a => bot and a <= top``
   * even and less than 100
       i % 2 == 0 and i < 100

Else
-----------------
 * if then makes sense
 * else is what you do if the conditional is false

::
    if answer == "yes":
        runProgram()
    else:
        sys.exit()

 * what if you want to check for multiple things
 * use elif (else if)

::
    if name == "Paul":
        print "You a teacher"
    elif name == "Alec" or name == "Jonah":
        print "You a TA"
    else:
        print "You a troll"


Using it together
-------------------------
 * `Running Total <d4ex4.py>`_
 * `Pygame Example <d4ex5.py>`_
