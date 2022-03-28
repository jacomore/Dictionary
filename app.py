import pandas as pd
import numpy as np

dictionary = pd.read_csv('english_computational.csv',header = None,index_col = False, dtype = str)
dictionary = dictionary.rename(columns = {0:'WORD', 1:'MEANING'})

nwords = dictionary.last_valid_index() + 1

for s in range(0,nwords+1):
    english = dictionary.rename(index= lambda s:s+1)

again = 'yes'

word = 'right'
word = 'left'

if word == 'right':
    while again in ['y', 'Y', 'yes','yess', 'Yes', 'YES']:
        rand_word = np.random.randint(1,nwords+1)
        print(english.at[rand_word,'WORD'])
        want_know = input('Do you need the translation? ')
        if want_know in ['y', 'Y', 'yes','yess' 'Yes', 'YES']:
            print(english.at[rand_word,'MEANING'])
        again = input('Do you want to proceed?')
else:
    while again in ['y', 'Y', 'yes','yess','Yes', 'YES']:
        rand_word = np.random.randint(1,nwords+1)
        print(english.at[rand_word,'MEANING'])
        want_know = input('Do you need the word?')
        if want_know in ['y', 'Y', 'yes','yess','Yes', 'YES']:
              print(english.at[rand_word,'WORD'])
        again = input('Do you want to proceed?')

