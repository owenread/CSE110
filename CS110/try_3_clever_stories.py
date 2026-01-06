#I decided to make some of the words fully uppercase to add more drama
#and emotion to the story. I also added a another adjective, an adverb, 
#and another sentance to the story to make the reader feel like the author
#really wanted them to feel the emotion of the crazy trouble they were in.
#I hope you enjoyed it!

#Request words for the Mad Lib
print('Please enter the following: ')
print('')

adjective_1 = input('Adjective: ')
animal = input('Animal: ')
verb_1 = input('Verb: ')
exclamation = input('Exclamation: ')
verb_2 = input('Verb: ')
verb_3 = input('Verb: ')
#added inputs
adjective_2 = input('Adjective: ')
adverb = input('Adverb: ')
print('')
#Display the Mad Lib in proper format with added final sentance. 
print(f'The other day, I was really in trouble. It all started when I saw a VERY\n' \
f'{adjective_1.upper()} {animal.upper()} {verb_1.upper()} down the hallway. "{exclamation.upper()}!" \n' \
f'I yelled. But all\n I could think was to {verb_2.lower()} over and over. Miraculously,\n' \
f'that caused it to stop, but not before it tried to {adverb.upper()} {verb_3.upper()} \n' \
f'right in front of my family. To be fair, what would you do when a very\n' \
f'{adjective_2.lower()} {adjective_1.lower()} {animal.lower()} {verb_1.lower()} \n' \
f'just before it almost tried to {verb_3.upper()}\n in front of your own family!?')