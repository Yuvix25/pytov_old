[comment]: <> (README for github)
# pytov [![Documentation Status](https://readthedocs.org/projects/pytov-documentations/badge/?version=latest)](https://docs.pytov.ml/en/latest/?badge=latest)


Python but tov (good).  

[Examples](https://github.com/Yuvix25/pytov/tree/master/pytov/examples)  
[Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=Yuvix25.pytov-run)


## Features
* Curly braces (not must)
* No identation errors (if you use the curly braces)
* func or function instead of def
* Long and short comments (`/**/`, `//`)
* Short boolean operators (`and` - `&&`, `or` - `||`, `not` - `!`)
* Lower case true and false supported too
* Switch statement
* Compiles to python

## Requirements
* python 3

## How to use
First, run `$ pip install pytov`, and then, to run files, simply run in the command line `$ pytov path_to_file`.
If you want to also save the compiled python file use (`$ pytov path_to_file -py`).

## Syntax
```c#
if (1 && 1){
                   print("i dont care about indentation");
   if(1==1){
print("except");
}
       }
if (1!=2){
    print("\'ihihih\'");
    print({"hi":1}["hi"]);
}

def hi(){
    print("hi");
}

def hello(){
    print("hello\"");
}

print(true || false) // you don't have to use capital T and F in true and false.

def indentation():
    print("You don't have to use the braces, the regular indentation works too")


anotherTest()

dict = {"hello":1};

/*
this will not be an error
multi line
*/

//this one too

print(1 /_ 3) // floor division

switch("hii", {
    "hello":
        lambda{ print("hello"); },
    "hi":
        lambda{ print("hi"); },
    },
        lambda{ print("default case"); },
);
```

The sample above shows use of pytov syntax.

Just like C, use curly braces instead of colons (but they still work too), and there are no more indentation errors.
```c#
def test(){
        print("no identation errors")
    pass
}
if (1 == 1){
    pass
}
```

### Switch
`switch(var, cases, *args)`
* var - the value to switch on.
* case - a dictionary of case that the var might be and their callbacks.
* *args(optional) - default case.

switch is a selection statement that chooses a single switch section to execute from a list of cases.


### Comments

Multiline:
```c#
/*
use this syntax if you want the text to be commented out
and yes, it works on multiple lines.
*/
```
Single line
```c#
// you can also write single line comments like this
```

### Short boolean operators
Instead of:
```python
if True and False:
    pass
elif True or False:
    pass
elif not True:
    pass
```
you can now use (pass no required):
```c#
if true && false{
    
}
elif true || false{
    
}
elif !true{
    
}
```

---
[Full documentation](https://docs.pytov.ml)

---
