# Strings
 * strings are a "sequence of characters" (best definition I could find)
 * A character is a single letter, number, symbol
    * like 'a', '4', '!', ' ',
    * anything you can create with "one key press"
* Strings are immutable
   * once you create a string you cannot change it
   * joining it with other strings or taking off chunks simply creates new a string
   * normally, this isn't an issue unless you add millions of strings together one at letter at a time

## Ways to Create a String:
`python
# single quotes
'To be or not to be'

# double quotes
"...it has the words DON'T PANIC inscribed in large friendly letters on its cover"

# triple quotes
"""
You can write this with either triple " or ', it doesn't matter.  But
by far the coolest part is that you can continue writing this string
on multiple lines and it doesn't care!!!
""" 
`

## Escaping and Special characters in strings:
Let's say you want to have a string which has the following sentence.

`She shouted, "I'd like a cup of tea!"`

You would run into trouble putting it in single quotes:

`'She shouted, "I'd like a cup of tea!"'`

Everything after the second `'` is _outside_ of the string and would crash the program.  You'd have the same trouble with a double quote `"`

To get around this, there are escape sequences.  Each sequence starts with the escape character (in python ` \ `) which tells the language to treat whatever follows differently.  So `\'` means single quote and `\"` means double.  The string can be created like this.

`'She shouted, "I\'d like a cup of tea!"'`

* There are lots of other uses
* Print a triple quoted string, and you get all the line breaks.  _try it_
* if you wanted to put line breaks in your code (so you can read it) but not have them show up in the string, you can use the escape character.
```python
>>> "This is the first line...\
... and this is the second"
'This is the first line...and this is the second.'
```
* certain characters mean specific things
   * `\n` means newline
   * `\t` means tab
* to have a single backslash, use `\\`

## Raw strings:
* this rarely comes up, but for things like filenames in windows, you can make a raw string which doesn't use escape sequences.  They start with `r` or `R`
```python
>>> r"Newlines are created with \n"
'Newlines are created with \\n'
>>> R"C:\Users\myname\My Documents"
'C:\\Users\\myname\\My Documents'
```
> skip unicode, shouldn't come up in game development, or just mention they exist, probably to deep this early on and should be addressed as needed later

