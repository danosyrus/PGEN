import PySimpleGUI as sg
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def generate_random_password():
	random.shuffle(characters)
	password = []
	for i in range(random.randint(5, 15)):
		password.append(random.choice(characters))

	random.shuffle(password)
	return ("".join(password))

layout = [[sg.Text(size=(40,1), key="output")], 
          [sg.Button("Generate Password")]]
sg.theme("dark grey")
window = sg.Window("Password Generator", layout)

while True:
    event, values = window.read()
    window["output"].update(generate_random_password(),text_color="yellow")

window.close()
