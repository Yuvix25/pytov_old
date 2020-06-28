
# pytov
Python but tov (good).

## Features
* Curly braces
* No identation errors
* Long and short comments (`/**/`, `//`)
* Short boolean operators (`and` - `&&`, `or` - `||`, `not` - `!`)
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
                   print("i dont care about indetation");
   if(1==1){
print("except");
}
       }
if (1!=2){
    print("ihihih");
    print({"hi":1}["hi"]);
}

def hi(){
    print("hi");
}

def hello(){
    print("hello");
}


dict = {"hello":1};

/*
this will not be an error

*/

//this one too



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

Just like C, use curly braces instead of colons (they will not work), and there are no more identation errors.
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
* case - a dictionery of case that the var might be and their callbacks.
* *args(optional) - default case.

switch is a selection statement that chooses a single switch section to execute from a list of cases.


### Multiline comments
```c#
/*
use this syntax if you want the text to be commented out
and yes, it works on multiple lines.
*/

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
you can now use:
```c#
if True && False{
    pass
}
elif True || False{
    pass
}
elif !True{
    pass
}
```