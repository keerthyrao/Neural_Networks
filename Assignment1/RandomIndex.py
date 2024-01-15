# Python program to delete at least 2 characters, reverse the resultant string and print it
import random
# Python program to randomly delete at least 2 characters, reverse the resultant string and print it
string = input("Enter a string: ")  # Get input string from console
# Convert the string to a list of characters
char_list = list(string)
# Randomly delete at least 2 characters
if len(char_list) > 2:  # Ensure at least 2 characters remain
    random_no_indexes=random.randrange(2, len(char_list))
    #print("No of random indexes generayed :", random_no_indexes)
    for i in range(random_no_indexes):
        random_index= random.randrange(len(char_list))
        #print("generated indexe is:",random_index)
        del char_list[random_index]
    # Join the reversed list of characters back into a string
    print(''.join(char_list[::-1]))
else: print("input string must have atleast 2 characters")



