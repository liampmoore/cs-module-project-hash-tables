


UNderstand:

INputs:

We have an ordered set of numbers `q`, which can have any numbers in it
(no duplicates).
```
q = (1, 3, 4, 7, 12)
```

And we have a function `f(x)`, which is defined as:

```
f(x) = x * 4 + 6
```

Output:
What are the combinations of `f(a) + f(b)` that are algebraically
equivalent to the combinations of `f(c) - f(d)`?


Plan:

Rough ideas:

Step 1:
Create a cache for f() values. Cache every calculation of f() as you build up the ab table and the cd table.

Step 2:
Create a table for ab combinations.
Iterate through every combination of a + b.
If an answer hasn't been generated yet create as a value in the table and add the combination as a dict to that list. {a: b: }

Step 3:
Do the same thing for cd combinations table.

Step 4:
Create a list to hold all permutations.
For every ab combo, if the same answer/key exists in the cd cache and none of the values are shared between the tables, add (a,b,c,d) combo to a list.

Step 5:
Return the list and the f() table.

Step 6:
Iterate through the list of abcd combos and print the statement for each, using the f cache.