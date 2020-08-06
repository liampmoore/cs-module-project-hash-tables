"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
def generate_permutations(input_nums, input_func):
    f_table = {}
    ab = {}
    cd = {}

    # first we build up two tables, one whose keys are answers to all possible f(a) + f(b) and values are said a and b values,
    # and a second table for the same with f(c) - f(d)
    # we cache answers to f(x) where we can and reuse them, as well as use them later when printing our output
    for num_a in input_nums:
        for num_b in input_nums:
            if num_a not in f_table:
                f_table[num_a] = input_func(num_a)
            if num_b not in f_table:
                f_table[num_b] = input_func(num_b)
            ab_sum = f_table[num_a] + f_table[num_b]
            cd_sum = f_table[num_a] - f_table[num_b]
            ab_entry = {}
            ab_entry["a"] = num_a
            ab_entry["b"] = num_b
            if ab_sum not in ab:
                ab[ab_sum] = [ab_entry]
            else:
                ab[ab_sum].append(ab_entry)
            cd_entry = {}
            cd_entry["c"] = num_a
            cd_entry["d"] = num_b
            if cd_sum not in cd:
                cd[cd_sum] = [cd_entry]
            else:
                cd[cd_sum].append(cd_entry)
    
    
    # we make a list of all permutations
    permutations = []
    # loop through every answer/key in a + b table
    for (key, ab_entries) in ab.items():
        # if an equivelent answer is in c - d table
        if key in cd:
            # loop through every possible f(a) + f(b) = f(c) - f(d) combination
            for ab_entry in ab_entries:
                for cd_entry in cd[key]:
                    # add the permutation to our list of permutations
                    permutations.append((ab_entry['a'], ab_entry['b'], cd_entry['c'], cd_entry['d']))
    # return our permutations values and our cached f(x) answers
    return (permutations, f_table)




(permutations, f_table) = generate_permutations(q, f)

# print permutations and corresponding f(x) values
for combination in permutations:
    print(f"f({combination[0]}) + f({combination[1]}) = f({combination[2]}) - f({combination[3]})    {f_table[combination[0]]} + {f_table[combination[1]]} = {f_table[combination[2]]} - {f_table[combination[3]]}")

