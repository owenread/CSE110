# Request words for the Mad Lib
print('Please enter the following:\n')

adjective_1 = input('Adjective: ')
animal = input('Animal: ')
verb_1 = input('Verb: ')
exclamation = input('Exclamation: ')
verb_2 = input('Verb: ')
verb_3 = input('Verb: ')
# added inputs
adjective_2 = input('Adjective: ')
adverb = input('Adverb: ')
print('')

# Display the Mad Lib in proper format with added final sentence
story = f"""
The other day, I was really in trouble. It all started when I saw a VERY
{adjective_1.upper()} {animal.upper()} {verb_1.upper()} down the hallway. "{exclamation.upper()}!"
I yelled. But all I could think was to {verb_2.lower()} over and over. Miraculously,
that caused it to stop, but not before it tried to {adverb.upper()} {verb_3.upper()}
right in front of my family. To be fair, what would you do when a very
{adjective_2.lower()} {adjective_1.lower()} {animal.lower()} {verb_1.lower()}
just before it almost tried to {verb_3.upper()}
in front of your own family!?
"""

print(story)
