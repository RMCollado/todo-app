import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a To-Do")
input_box = Sg.InputText(tooltip="Enter todo")
add_button = Sg.Button("Add")

window = Sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
