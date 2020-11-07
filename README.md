# brainf python compiler

My simple take on a BrainF compiler written in python.

Note that this does not support loops inside of eachother.

Here is some sample usage:

```txt
PS C:\Users\Evan\bf> pypy3 bf.py
bf< ,
bf<<< 21
bf< .
bf> 21
bf< >
bf< .
bf> 0
bf< ,
bf<<< 99
bf< .
bf> 99
bf< <
bf< .
bf> 21
bf< [
bf<< ->+<
bf<< ]
bf< .
bf> 0
bf< >
bf< .
bf> 120
bf<
```
