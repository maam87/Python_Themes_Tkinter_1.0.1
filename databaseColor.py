import sqlite3 as sq


def systemColor():
    connect = sq.connect('ListColor.db')
    cursor = connect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS ListColor 
                    (ID integer primary key, themesName text, primary_ text, secondary text, success text, info text, 
                    warning text, danger text, light text, dark text, background text, foreground text, select_foreground text,
                    select_background text, border text, input_foreground text, input_background text)''')

    ListOfColor = [
        ["cosmo", "#2780e3", "#7E8081", "#3fb618", "#9954bb", "#ff7518", "#ff0039", "#F8F9FA",
                    "#373A3C", "#ffffff", "#373a3c", "#7e8081", "#ffffff", "#ced4da", "#373a3c", "#fdfdfe"],
                   ["flatly", "#2c3e50", "#95a5a6", "#18bc9c", "#3498db", "#f39c12", "#e74c3c", "#ECF0F1",
                    "#7B8A8B", "#ffffff", "#212529", "#95a5a6", "#ffffff", "#ced4da", "#212529", "#ffffff"],
                   ["liter", "#4582ec", "#adb5bd", "#02b875", "#17a2b8", "#f0ad4e", "#d9534f", "#F8F9FA",
                    "#343A40", "#ffffff", "#343a40", "#adb5bd", "#ffffff", "#bfbfbf", "#343a40", "#fff"],
                   ["minty", "#78c2ad", "#f3969a", "#56cc9d", "#6cc3d5", "#ffce67", "#ff7851", "#F8F9FA",
                    "#343A40", "#ffffff", "#5a5a5a", "#f3969a", "#ffffff", "#ced4da", "#696969", "#fff"],
                   ["lumen", "#158cba", "#919191", "#28b62c", "#75caeb", "#ff851b", "#ff4136",
                    "#F6F6F6", "#555555", "#ffffff", "#555555", "#919191", "#ffffff", "#ced4da", "#555555", "#fff"],
                   ["sandstone", "#325D88", "#8e8c84", "#93c54b", "#29abe0", "#f47c3c", "#d9534f", "#F8F5F0",
                    "#3E3F3A", "#ffffff", "#3e3f3a", "#8e8c84", "#ffffff", "#ced4da", "#6E6D69", "#fff"],
                   ["yeti", "#008cba", "#707070", "#43ac6a", "#5bc0de", "#e99002", "#f04124", "#EEEEEE",
                    "#222222", "#ffffff", "#222222", "#707070", "#ffffff", "#cccccc", "#222222", "#fff"],
                   ["pulse", "#593196", "#69676E", "#13b955", "#009cdc", "#efa31d", "#fc3939", "#F9F8FC",
                    "#17141F", "#ffffff", "#444444", "#69676e", "#ffffff", "#cbc8d0", "#444444", "#fdfdfe"],
                   ["united", "#e95420", "#aea79f", "#38b44a", "#17a2b8", "#efb73e", "#df382c",
                    "#E9ECEF", "#772953", "#ffffff", "#333333", "#aea79f", "#ffffff", "#ced4da", "#333333", "#fff"],
                   ["morph", "#378DFC", "#aaaaaa", "#43cc29", "#5B62F4", "#FFC107", "#E52527", "#F0F5FA",
                    "#212529", "#D9E3F1", "#7B8AB8", "#aaaaaa", "#FBFDFF", "#B9C7DA", "#7F8EBA", "#F0F5FA"],
                   ["journal", "#eb6864", "#aaaaaa", "#22b24c", "#336699", "#f5e625", "#f57a00",
                    "#F8F9FA", "#222222", "#ffffff", "#222222", "#aaaaaa", "#ffffff", "#ced4da", "#565656", "#fff"],
                   ["darkly", "#375a7f", "#444444", "#00bc8c", "#3498db", "#f39c12", "#e74c3c", "#ADB5BD",
                    "#303030", "#222222", "#ffffff", "#555555", "#ffffff", "#222222", "#ffffff", "#2f2f2f"],
                   ["superhero", "#4c9be8", "#4e5d6c", "#5cb85c", "#5bc0de", "#f0ad4e", "#d9534f", "#ABB6C2",
                    "#20374C", "#2b3e50", "#ffffff", "#526170", "#ffffff", "#222222", "#ebebeb", "#32465a"],
                   ["solar", "#bc951a", "#94a2a4", "#44aca4", "#3f98d7", "#d05e2f", "#d95092", "#A9BDBD",
                    "#073642", "#002B36", "#ffffff", "#0b5162", "#ffffff", "#00252e", "#A9BDBD", "#073642"],
                   ["cyborg", "#2a9fd6", "#555555", "#77b300", "#9933cc", "#ff8800", "#cc0000", "#ADAFAE",
                    "#222222", "#060606", "#ffffff", "#454545", "#ffffff", "#060606", "#ffffff", "#191919"],
                   ["vapor", "#6e40c0", "#ea38b8", "#3af180", "#1da2f2", "#ffbd05", "#e34b54", "#44d7e8",
                    "#170229", "#190831", "#32fbe2", "#461a8a", "#ffffff", "#060606", "#bfb6cd", "#30115e"],
                   ["simplex", "#d8220e", "#858e96", "#469307", "#0099ce", "#d88220", "#9a479e", "#f2f2f2",
                    "#3b3d3f", "#fcfcfc", "#3b3d3f", "#a9afb6", "#ffffff", "#858e96", "#3b3d3f", "#fcfcfc"],
                   ["cerulean", "#4bb1ea", "#a9b4be", "#84b251", "#225384", "#e16e25", "#cf3c40", "#eceef1",
                    "#33383e", "#ffffff", "#2ea4e7", "#adb5bd", "#ffffff", "#a9b4be", "#495057", "#ffffff"]
                   ]

    for x in ListOfColor:
        cursor.execute('''Insert into ListColor (themesName, primary_, secondary, success, info, warning, danger,
                        light, dark, background, foreground, select_foreground, select_background, border, input_foreground,
                        input_background) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', x)

    connect.commit()
    connect.close()