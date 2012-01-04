# Functions

## Example of when to use a function
Let's see what we can do with this dictionary.  Download the module. Import into interpreter. Print it.

"Wow, that's hard to read"

_"Gee, I wish there were a better way"_ moment

## What is a function?
* functions are reusable pieces of code
* attach a name to a block of code and then you can run that block later using the same name `note: don't like this phrasing` 
* functions are defined using `def`, here's a basic structure

```python
def func():
    # code

```

> point out def, the name, the doc string, and what it does

**Example:**
```python
def greet():
    "Says hello"
    print "Hello, person"

>>> greet()
"Hello, person"
```

## Parameters
* functions can also take parameters, which are values supplied when you call a function
* parameters are also known as arguments
* like in math, when f(x) = x+3,  f(2)=5
* parameters work just like variables
   * you define them by calling the function

```python

def pprint(a):
    "A prettier way to print lists and dictionaries"
    if type(a) is list:
        for i,v in enumerate(a):
            print "%d: %s" % (i,v)
    elif type(a) is dict"
        for k,v in a.items():
            print "%d: %s" % (k,v)
    else:   
        print a

```

## Local/Global variables
* local variables only exist within the block they were defined even if they have the same name

> basic local example, basic global example, setting x, running a func which prints it's value, and then printing x again

## Largish in class excercise/example


## Advanced Topics
 * Default Values
 * keywords
 * variable length
