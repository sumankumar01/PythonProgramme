import pickle

imelda = ('suman',
          'kumar',
          '08-june-1991',
          ((1, 'pulling'),
           (2, 'psyco')))
print(imelda)

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)
