import itertools
#import string as st

string = input('Palavra para permutar: ')
#string = st.ascii_letters

resultado = itertools.permutations(string, len('string'))

for i in resultado:
    print(''.join(i))