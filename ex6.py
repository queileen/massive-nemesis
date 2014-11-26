# %d holds the place of the digit '10'
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# %s holds the place of the string 'binary' and then, 'do_not'
y = "Those who know %s and those who %s." % (binary, do_not)
print x
print y

# Terminal, print the string held by variable x
print "I said: %r." % x
# Terminal, print the string held by variable y
print "I also said: '%s'." % y

# False is held by the variable 'hilarious'
hilarious = False
# The string is held by the variable 'joke_evaluation' and print what is above with it also
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e