'''
Hashing

What if we are able to know which item has been placed where, such that searching
can be done in `O(1)` time?

The mapping between an item and the slot where that item belongs in the hash table
is called the hash function.

By design, Python automatically uses a hash datastructure when initialising
a list like `x = [1, 2, 4]`. Thus, callable by index like `x[0]` will return 1.

Maps
----
Hashing can be done in a custom way too. Even you can write a custom hash function
to figure out the position of any element (string, number etc.). Python also has a
default data structure for this - called a `Dictionary`

'''
