print "Welcome to the Pyg Latin Translator!"

original = raw_input("Enter a word:") # asks for the user's word
pyg = "ay" # the 'ay' suffix will be added to each word

if len(original) > 0 and original.isalpha(): #prints the user's input if the input is not an empty string and not composed of non-word characters
    print original + " is a nice word!" #confirms the word choice
    print original.lower() # shows step 1 i.e. conversion to lower case
    first_letter = original.lower()[0] # step 2 shows the first letter which will be removed
    print first_letter
    remainder = original[1:len(original)] # step 3 shows the remainder of the word
    print remainder
    new_word = remainder + pyg # step 4 shows the the remainder of the word with the pyg suffix
    print new_word # shows the transated word
    print "Your word translates to " + new_word + " in Pyg Latin!"
    print "Thank you for using our services."
else:
    print "Please try again!"
