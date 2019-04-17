string = str(input())
new_str = string[:17]+" in Dimigo"+string[17:26]+'y'+string[27:]
print(new_str)
print("-".join(new_str))