# My original list of things

things = ["Tokyo", "Paris", "New York", "Sydney", "Rome"]

print("Original list:", things)             # raw list
print("First item:", things[0])             # indexing
things[1] = "London"                        # modify
things.append("Berlin")                     # append
things.insert(2, "Madrid")                  # insert
things.remove("Tokyo")                      # remove
things.pop()                                # pop last
del things[0]                               # del

print("Sorted (temp):", sorted(things))     # sorted
print("Sorted reverse (temp):", sorted(things, reverse=True))
things.sort()                               # sort
things.reverse()                            # reverse
print("Final list:", things)                
print("Number of items:", len(things))      # len