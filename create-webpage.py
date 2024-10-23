# Hope Cano
# create-webpage.py
# October 22 2024
# CISW 24

import os
import sys

# this section will ask the user to input a file name
file_name = input("Enter the character name for the file (no spaces, use lowercase): ").strip()
out_file = f"{file_name}.html"

# this section will ask the user to input the character name
body_h1 = input("Enter the character's name: ").strip()
body_h1 = f"<h1>{body_h1}</h1>\n"

# this section will ask the user to input actor's name
body_h2 = input("Enter the actor's name: ").strip()
body_h2 = f"<h2>Played by {body_h2}</h2>\n"

# this section will ask the user to input a description of the character
body_description = input ("Enter a brief description of the character: ").strip()
body_description = f"<p>{body_description}</p>\n"

# this section will ask the user to input the location of an image file of the character they either downloaded locally, or via a url
body_img = input("Enter the image file location (URL or local path): ").strip()
body_img = f'<img src="{body_img}" alt="{file_name}">\n'

# this section will ask for the character quote
character_quote = input("Enter a quote from the character: ").strip()
character_quote = f'<blockquote>{character_quote}</blockquote>\n'

# this section will ask for the YouTube embed link
youtube_link = input("Enter the YouTube embed link of the character: ").strip()
youtube_link = f'<iframe width="560" height="315" src="{youtube_link}" frameborder="0" allowfullscreen></iframe>\n'

#this section comines the user inputs in a single variable
combined_body = f"{body_h1}{body_h2}{body_description}{body_img}{character_quote}{youtube_link}"

# Correcting the file path using os.path.join
with open(os.path.join('assets', 'page-head.txt'), 'r') as f:
    combined_head = ''.join(f.readlines())

with open(os.path.join('assets', 'page-footer.txt'), 'r') as f:
    combined_footer = ''.join(f.readlines())

# concatenate the head, body, and footer sections into a single HTML page
combined_page = combined_head + combined_body + combined_footer

# This notifies the user that the file has been created
with open(out_file, "w") as f:
    f.write(combined_page)
print("Created {}".format(out_file))
