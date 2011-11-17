==============================
Datatypes and Variables
==============================
Day 3 [1.W] (2/1)
------------------------------

Data
===============
 * Just like before when we printed things, those
 * Basic types
    * numbers
    * booleans
    * strings
 * we will see others like lists, dictionaries, and objects later

Integers
--------------
 * Integers
    * integers.  positive/negative whole numbers
    * 2, -3, 0
 * Longs:  really really big integers.  
    * 1000000000000000000000000000000000000000000000000L
 * python should convert between these two types automatically if your integers get too big
 * Longs end in a "L", don't worry about it if you see one

Floats
----------------
* A number with a decimal
    * 3.5, -0.23
* called floats because of floating decimal points
    * _coders_ actually a double
* can also be written in scientific notation
    * -5.23E-4

Operators
--------------
 * ``+``, ``-``, ``*``, ``/ ``, ``%``, ``**``

Example
::
  >>> 3 / 2
  1
  >>> 3 / 2.0
  1.5

Converting
--------------
 * ``int()`` and ``float()``


Booleans
-----------------
* True or False


Variables
==============
Now that there is data, there needs to be a way to store it and get to it. There needs to be a way to pass information you get to other parts of your program.  Creating variables couldn't be easier, you simply give them a name.  This is refered to as an "identifier", it is what you use to identify part of your code.

* valid identifiers can start with `_` or a letter
* the rest can be a `_`, a letter, or a number
* valid names: `i`, `myName`, `string2int`, `__ignoreMe`, `a23_32`
* invalid names: `99problems`, `my name`, `bad-name`

Using variables
-----------------
You can use variables to store any python object (everything, including numbers is an object).  

::
    >>> i = 5
    >>> print i
    5
    >>> i = i + 1
    >>> print i
    6

::
   >>> w,h = 3,4
   >>> print "Area is:", w * h
   12
   >>> print "Perimeter is:", w + w + h + h
   14

| Above is what is known as unpacking


Reading Input and Strings
=============================
The other type of data we have already used is strings, the things in the double quotes.  You can think of strings as

Strings
-------------
 * strings are a "sequence of characters" (best definition I could find)
 * A character is a single letter, number, symbol
    * like 'a', '4', '!', ' ',
    * anything you can create with "one key press"
* Strings are immutable
   * once you create a string you cannot change it
   * joining it with other strings or taking off chunks simply creates new a string
* you can create using single or double quotes, though double are usually preferred

Input
----------------
 * input from the user with "raw_input(prompt)"
 * Ex 1: hello name
    * `see example 1 <d3ex1.py>`_
 * EX 2: getting some numbers and doing a couple of equations
    * `see example 2 <d3ex2.py>`_
    * explain string substitution
       * there is a lot more on this subject, but for debuging it can't be beat
 * EX 3: printing dyamind
   * `see example 3 <d3ex3.py>`_
