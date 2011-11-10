# Variables
Now that there is data, there needs to be a way to store it and get to it. There needs to be a way to pass information you get to other parts of your program.  Creating variables couldn't be easier, you simply give them a name.  This is refered to as an "identifier", it is what you use to identify part of your code.

* valid identifiers can start with `_` or a letter
* the rest can be a `_`, a letter, or a number
* valid names: `i`, `myName`, `string2int`, `__ignoreMe`, `a23_32`
* invalid names: `99problems`, `my name`, `bad-name`

## Using variables
You can use variables to store any python object (everything, including numbers is an object).  

``python
>>> i = 5
>>> print i
5
>>> i = i + 1
>>> print i
6
>>> s = '''this is a multiline string
in my source code'''
>>> print s
this is a multiline string
in my source code
``

## naming conventions
* _coders_:  other languages use things like toString, or myDocumentObject, python as a rule prefers `_` or as one word
  * `tostring` or `to_string`
  * the other is still valid
* an identifier in all capitals is usually global constant.  More on global later, but constant means that it should never change
  * `PI`, `SCREEN_SIZE`
  * _coders_: python has no way of declaring something "constant", naming it this way tells other coders to leave the variable alone
* an identifier which starts with `_` is usually private.  This means that if you didn't define it, you probably aren't meant to use it because it is internal to the library, more on this later. 
    * _coders_: python has no way of declaring something private, again use the convention

