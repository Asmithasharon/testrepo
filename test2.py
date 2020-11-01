import PySimpleGUI as sg
layout = [
    [sg.Listbox(["apple","mango", "orange"], size = (40, 5), font = ("Arial", 14), key = 'list1')],
    [sg.Button("OK"),sg.Button("Exit")]
]


window = sg.Window("First App", layout)
events, values = window.Read()
print(events)
print(values)


window.Close()
