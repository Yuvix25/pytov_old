# Pytov's syntax

## Blocks

In pytov, blocks are now better.  
You dont use colons to start a block, to use identation (and to get identation error).  
With pytov, you simply start a block with `{` and end it with `}` (see example bellow), and the best part, the identation doesn't matters!

```python
if True{
    print("pytov")
}
```

## Comments

### **Multiline**

In python, there are no multiline comments only `"""not a real comment, just a string"""`, but it gives you an error from time to time.  
So to fix that, in pytov you can use multiline comments with bellow syntax.
```c#
/*
This is a multiline comments
Just like in C languages (and almost every programming language except python), all you need to do, is just start it with / and *, and end it with * and /
*/

print("the above text will not execute, because it is a comment, but this code will.")
```

### **Single Line**

If before comming to python you programmed in other languages, you might got a few syntax errors on using `//` instead of `#` for single line comments, so to solve this issue, in pytov `//` this a single line comment too, and to perform floor division (originally by `//`) you can now use `/_` .