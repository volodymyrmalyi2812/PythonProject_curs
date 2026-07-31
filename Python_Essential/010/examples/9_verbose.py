import re

pattern1 = '^L{0,3}(CM|CD|D?C{0,3})(XC|XL|M?X{0,3})(IX|IV|V?I{0,3})$'
print(re.search(pattern1, 'LDMV'))

pattern2 = """
    ^ - start
    L{0,3}
    (CM|CD|D?C{0,3})
    (XC|XL|L?X{0,3})
    (IX|IV|V?I{0,3})
    $ - end
    """
print(pattern2)
re.search(pattern2, 'LDLV', re.VERBOSE)

# Використання прапора компіляції
re.compile('''
           [\w\.-]+
           @
           [\w\.-]+'
           ''',
           re.VERBOSE)
