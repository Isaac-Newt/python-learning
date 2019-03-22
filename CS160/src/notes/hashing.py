# Rehash function: rehash(pos) = (pos + skip) % table_size (not length, but number of slots)

# Retrieval algorithm:
#
# Hash the value
# Look up in table
# If there, return True
# Else continue linear search until either item or empty slot is found

# Another solution: Chaining
# Less efficient

# Quadratic Probing
# Skip value is the square of the number of collisions at that index
# i.e. 1, 4, 9, 16, ...
# Reduces clustering of data