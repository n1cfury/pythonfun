# Python Excuse Generator v1.0
# Generate random excuses from the three different columns
import random

intro = [
    "Sorry I can't come ",
    "Please forgive my absence ",
    "This is going to sound crazy but ",
    "Get this: ",
    "I can't go because ",
    "I know you're going to hate me but ",
    "I was minding my own business and boom ",
    "I fell terrible but ",
    "I regretfully cannot attend ",
    "This is going to sounds like an excuse but "
]

scapegoat = [
    "My nephew ",
    "the ghost of Hitler ",
    "the Pope ",
    "my ex ",
    "a high school marching band ",
    "Dan Rather ",
    "a sad clown ",
    "the kid from Air Bud ",
    "a professional cricket team ",
    "my Tinder date "
]

delay = [
    "just shit the bed.",
    "died in front of me."
    "won't stop telling me knock knock jokes.",
    "is having a nervous breakdown.",
    "gave me syphillis.",
    "poured lemonade in my gas tank"
    "stabbed me.",
    "found my box of human teeth.",
    "stole my bicycle.",
    "posted my nudes on Instagram."
]

print ("")
print ("Python Excuse Generator")
print ("Found a Meme with random excuses,")
print ("I decided to make an excuse generator")
print ("and this one generates them randomly")
print ("")
print (random.choice(intro)) + (random.choice(scapegoat)) + (random.choice(delay))
