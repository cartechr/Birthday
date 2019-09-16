
birthday_dictionary = {
	"Carter": "5/4/2001",
	"Simon": "9/28/1999",
	"Cameron": "1/16/2002",
	"Gabi": "8/12/2001",
    "Jay" : "6/23/2001",
    "Sebastian" : "1/30/2000",
    "Kate" : "10/10/2004"
}


print ('>>> Welcome to the birthday dictionary. We know the birthdays of: \nCarter \nSimon \nCameron \nGabi \nJay \nSebastian \nKate')
print("\nWho's birthday do you want to look up?")
name = input()
if name in birthday_dictionary:
    print('{}\'s birthday is {}.'.format(name, birthday_dictionary[name]))
else:
	print('Sorry not in the dictionary :(')