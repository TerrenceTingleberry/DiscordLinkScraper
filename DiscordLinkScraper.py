import json
import re
import pyperclip
import time

# Set this to the path of your chat export
chatExport = 'C:\Files\Programming\Files\Python\DiscordLinkScraper\Chat Exports\link-queue.json'

# Load the JSON data from the file
with open(chatExport, encoding='utf-8') as f:
    data = json.load(f)

links = []
for message in data['messages']:
    # Extract links from message content
    links_in_message = re.findall(r'(?:https?|ftp|file):\/\/(?:ww(?:w|\d+)\.)?((?:[\w_-]+(?:\.[\w_-]+)+)[\w.,@?^=%&:\/~+#-]*[\w@?^=%&~+-])', message['content'])
    # Append links to the list of links
    links.extend(links_in_message)

if links:
    # Convert the list of links to a string separated by newline character
    links_string = '\n'.join(links)
    # Copy the links string to the clipboard
    pyperclip.copy(links_string)
    # Print the number of links copied to the clipboard
    print(f"Copied {len(links)} links to clipboard.")
else:
    # If no links were found, print "No links found in the message(s)."
    print("No links were found in the message(s).")

# Pause for 5 seconds before exiting
time.sleep(0.5)

# Wait for the user to press ENTER to end execution of the script.
input("Press ENTER to exit")
