def word_count(s):
    # Your code here
    table = {}
    current = ''
    for i, c in enumerate(s.lower()):
        if c >= 'a' and c <= 'z' or c == "'":
            current = current + c
        else:
            if current != '':
                if current not in table:
                    table[current] = 1
                    current = ''
                else:
                    table[current] += 1
                    current = ''
    if current != '':
                if current not in table:
                    table[current] = 1
                    current = ''
                else:
                    table[current] += 1
                    current = ''
    return table      




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))