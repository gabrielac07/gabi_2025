---
layout: post
title: Safe Computing Hack 2
author: Gabriela Connelly
permalink: /safe_computing/
---

{% highlight python %}
import random

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():  # Encrypts only letters
            shift_amount = shift if mode == "encrypt" else -shift
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char  # Keeps spaces and punctuation unchanged
    return result

# Getting user input
mode = input("Do you want to encrypt or decrypt? ").strip().lower()
message = input("Enter your message: ")
shift_input = input("Enter shift value (number of places to shift) or type 'random': ").strip().lower()

# Handling the "random" shift value
if shift_input == "random":
    shift = random.randint(1, 25)
    print(f"Random shift value selected: {shift}")
else:
    shift = int(shift_input)

# Performing encryption/decryption
output = caesar_cipher(message, shift, mode)
print(f"Result: {output}")
{% endhighlight %}
