from dragonfly import Key, Text, Mouse
from mathfly.lib import utilities

# Alternate between executing as text and executing as keys
def alternating_command(command):
	if type(command) in [str, int, unicode]:
		Text(str(command)).execute()
	elif type(command) in [list, tuple]:
		for i in range(len(command)):
			if i%2==0:
				Text(command[i]).execute()
			else:
				Key(command[i]).execute()

def template(template):
	utilities.paste_string(template)