import sys

big_range=range(10000)
print("big range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containg all the value in big_range
big_list=[]

for val in  big_range:
    big_list.append(val)

print("big list is {} bytes".format(sys.getsizeof(big_list)))