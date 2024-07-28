#given string
A=['abc', 'xyz', 'aba', '1221']

# Iterate through the list with index
for index, string in enumerate(A):

    if len(string) > 0 and string[0] == string[-1]: #checking if the first and the last element are identical

        print(f"String is: '{string}' at index {index}")







