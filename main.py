#!/usr/bin/env python3
import sys
import random
from quotes import QUOTES

if len(sys.argv) > 1:
	quote = " ".join(sys.argv[1:])
else:
	quote = random.choice(QUOTES)

width = len(quote)

print(" " + "_" * (width + 2))
print(f"< {quote} >")
print(" " + "-" * (width + 2))

print(r"""
        \
         \
          🔮
       (ಠ_ಠ)
      /|   |\
       |   |
      / \ / \
""")
