a = [1, 2, 3, 4, 1]
max_el = 4

# Find the index of the maximum element
max_el_index = a.index(max_el)

min_el_after_max_index = max_el_index + 1 + a[max_el_index+1:].index(min(a[max_el_index+1:]))
print(f"The index of the minimum element after {max_el} is {min_el_after_max_index}")