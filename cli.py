import random

from quotes import QUOTES
from shamans import SHAMANS
from bubble import create_bubble

quote = random.choice(QUOTES)

print(create_bubble(quote))
print(SHAMANS["wizard"])
