# short_lambda

You are a busy python programming. You love functools and lambdas. But, 
lambda is such a long word, even worse you have to declare, the variables.
You don't have time for that. What you don't need, and I do not recommend 
you use is short_lambda. 

This was a bit of fun, just to see what could be achieved. Stay safe kids
and use a list comprehension. Or if needed use def, def is 3 fewer letters
than lambda. If we were supposed to do it, the core devs would have allowed 
javascript like syntax (x => x+2).

| Short Lambda | Lambda              |
|--------------|---------------------|
| `F(X+2)`     | `lambda x: x+2`     |
| `F(X//2)`    | `lambda x: x//2`    |
| `F(X==2)`    | `lambda x: x==2`    |
| `F(X<2)`     | `lambda x: x<2`     |
| `F(X())`     | `lambda x: x()`     |
| `F(X(3))`    | `lambda x: x(3)`    |
| `F(X.f(3))`  | `lambda x: x.f(3)`  |
| `F(X==2)`    | `lambda x: x==2`    |
| `F(X<2)`     | `lambda x: x<2`     |
| `F(X==Y)`    | `lambda x, y: x==y` |
| `F(X*Y)`     | `lambda x, y: x*y`  |

# Setup

Clone and run
```
pip install .
```
