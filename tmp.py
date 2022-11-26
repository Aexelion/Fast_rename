import PySimpleGUI as sg

sg.theme('DarkGrey14')

TMP = [f"E{i}" for i in range(100)]

layout_column1 = [
                    [sg.Listbox(values=TMP, key="-FILE_INPUT-", size=(30,10))],
                 ]
layout_column2 = [
                    [sg.Image("./fleche.png")],
                 ]
layout_column3 = [
                    [sg.Text("a\n"*10, key="-FILE_OUTPUT-", size=(20,10))]
                 ]
layout_column4 = [
                    [sg.Button("Add a file", key="-ADD_FILE-", size=(20,))],
                    [sg.Button("Update with regex", key="-UPDATE_REGEX-", size=(20,))],
                    [sg.Button("Delete file", key="-DEL_FILE-", size=(20,))],
                    [sg.Button("Delete all files", key="-DEL_ALL-", size=(20,))],
                    [sg.Text("_"*23)],
                    [sg.Button("Fast Rename !", key="-FAST_RENAME-", size=(20,2))],
                 ]


main_layout = [
                [sg.Text("Your fast rename solution\n")],
                ## Main part
                [sg.Frame("Input Files", layout_column1),
                 sg.Col(layout_column2),
                 sg.Frame("Output Files Preview", layout_column3),
                 sg.Col(layout_column4),
                ],
                ## Options
                [sg.Text()],
                [sg.Image("./bas.png"),\
                 sg.Text("Options"),
                ],
                [sg.Text("Current Regex :"),
                sg.Text("", size=(30,), key="-CURRENT_REGEX-")],
                [sg.Text("New Name :"),
                sg.Input(key="-NEW_NAME-", size=(30,)),
                sg.Checkbox("Keep Current Name", key="-KEEP_NAME-")
                ],
                [sg.Button("Change Regex", key="-CHANGE_REGEX-", size=(15))
                ],
         ]

window = sg.Window("Fast Rename", main_layout)





end = False
while not(end):
   event, values = window.read()
   if values :
      selected_file = values["-FILE_INPUT-"]
      keep_name = values["-KEEP_NAME-"]
      new_name = values["-NEW_NAME-"]
      current_regex = window["-CURRENT_REGEX-"].get()
   print(event, values)
   if event == sg.WIN_CLOSED or event == "Exit":
      end = True
   if event == "-ADD_FILE-" :
      pass
   if event == "-UPDATE_REGEX-" :
      pass
   if event == "-DEL_FILE-" :
      file_list = window["-FILE_INPUT-"].GetListValues()
      window["-FILE_INPUT-"].update([file for file in file_list if file not in selected_file])
   if event == "-DEL_ALL-" :
      window["-FILE_INPUT-"].update([])
   if event == "-FAST_RENAME-" :
      pass
   if event == "-CHANGE_REGEX-" :
      new_regex = sg.popup_get_text("/!\\ --- WARNING --- /!\\ \
         \nRegex are for confirm users,\
         \nif you don't know what this is close this window\
         \n/!\\ --- WARNING --- /!\\ \
         \n\nEnter a new regex to use :")
      if new_regex != None:
         window["-CURRENT_REGEX-"].update(new_regex)
   
window.close()

