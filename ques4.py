
ListColour = ["Black", "Red", "Maroon", "Yellow"]
ListHex = ["000000", "FF0000", "800000", "FFFF00"]

dict_list = []

# Using a loop to create the dictionaries and append them to the list
for i in range(len(ListColour)):
    dict_list.append({"Color": ListColour[i], "Hex": ListHex[i]})


print(dict_list)