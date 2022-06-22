#! python3
# bulletPointAdder.py - Add Wikipedia bullet points to the start.
# of each line of text on the clipboard.
# Some more line s- to add to git!
import pyperclip
text = pyperclip.paste()
# to do - seperate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
print(text)