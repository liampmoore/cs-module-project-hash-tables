# No Duplicates

Input: a string of words separated by spaces. Only the letters `a`-`z`
are utilized.

Output: the string in the same order, but with subsequent duplicate
words removed.

There must be no extra spaces at the end of your returned string.

The solution must be `O(n)`.


Plan:
Step 1:
Iterate through the string and add each letter to the hash table if it's not already There
for c in string:
    if c not in table:
        table[c] = c

Step 2:
Iterate through the table and add all the letters to an output string.
output = ''
for c in table:
    output = output + c

return output
    