from tkinter import ttk
import sqlite3 as sq


def Style(root):
    ThemesName = 'superhero'  # default theme
    try:
        with open("colorSystem.txt", "r") as file:
            ThemesName = file.read()
    except FileNotFoundError:
        # Save the current number to a file
        with open("colorSystem.txt", "w") as file:
            file.write(str(ThemesName))

    ThemesName = open('colorSystem.txt', 'r').read()

    # Primary
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    primary = cursor.fetchone()[2]  # select theme name input foreground color
    connect.commit()
    connect.close()

    # Secondary
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    secondary = cursor.fetchone()[3]  # select theme name input foreground color
    connect.commit()
    connect.close()

    # Success
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    success = cursor.fetchone()[4]  # select theme name input foreground color
    connect.commit()
    connect.close()

    # Info
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    info = cursor.fetchone()[5]  # select theme name input foreground color
    connect.commit()
    connect.close()

    # Warning
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    warning = cursor.fetchone()[6]  # select theme name input foreground color
    connect.commit()
    connect.close()

    # Danger
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    danger = cursor.fetchone()[7]  # select theme name input foreground color
    connect.commit()
    connect.close()

    # Light
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    light = cursor.fetchone()[8]  # select theme name input foreground color
    connect.commit()
    connect.close()

    # Dark
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    dark = cursor.fetchone()[9]  # select theme name input foreground color
    connect.commit()
    connect.close()

    # Background (bg)
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    bg = cursor.fetchone()[10]  # select theme name input foreground color
    connect.commit()
    connect.close()

    # Foreground (fg)
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    fg = cursor.fetchone()[11]  # select theme name foreground color
    connect.commit()
    connect.close()

    # Selected Foreground (select_fg)
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    select_fg = cursor.fetchone()[12]  # select theme name background color
    connect.commit()
    connect.close()

    # Selected Background (select_bg)
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    select_bg = cursor.fetchone()[13]  # select theme name background color
    connect.commit()
    connect.close()

    # Border
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    border = cursor.fetchone()[14]  # select theme name background color
    connect.commit()
    connect.close()

    # Input Foreground (input_fg)
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    input_fg = cursor.fetchone()[15]  # select theme name background color
    connect.commit()
    connect.close()

    # Input Background (input_bg)
    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    input_bg = cursor.fetchone()[16]  # select theme name background color
    connect.commit()
    connect.close()

    root.configure(background=bg)

    style = ttk.Style()
    style.theme_use('clam')
    style.theme_settings('clam', {
        'TCombobox': {
            'configure': {
                'padding': (10, 5, 10, 5),
                'background': bg,  # Default background color
                'foreground': fg,  # Default foreground color
                'font': 'Courier 12 bold italic',
            },
            'map': {
                'background': [('active', primary),
                               ('!disabled', bg),
                               ('readonly', bg),
                               ('disabled', secondary),
                               ('pressed', bg)],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('readonly', fg),
                               ('disabled', secondary),
                               ('pressed', select_fg), ]
            }
        },
        'TCombobox.Readonly': {
            'configure': {
                'padding': (10, 5, 10, 5),
                'background': bg,  # Default background color
                'foreground': fg,  # Default foreground color
                'font': 'Courier 12 bold italic',
            },
            'map': {
                'background': [('active', primary),
                               ('!disabled', bg),
                               ('disabled', secondary),
                               ('pressed', bg)],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary),
                               ('pressed', select_fg), ]
            }
        },
        'TLabelframe': {
            'configure': {
                'padding': (3, 2, 3, 2), 'bordercolor': border, 'relief': 'solid',
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg)],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary)]
            }
        },
        'TLabelframe.Label': {
            'configure': {
                'font': 'Courier 12 bold italic',
                'padding': (3, 2, 3, 2),
                'anchor': 'center',
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg)],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary)],
            }
        },
        'TFrame': {
            'configure': {
                'font': 'Courier 14 bold italic',
                'padding': (3, 2, 3, 2),
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg)],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary)]
            }
        },
        'TButton': {
            'configure': {
                'padding': (10, 5, 10, 5),
                'background': bg,  # Default background color
                'foreground': fg,  # Default foreground color
                'font': 'Courier 14 bold italic',
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('readonly', dark),
                               ('disabled', bg),
                               ('pressed', input_bg), ],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('readonly', light),
                               ('disabled', secondary),
                               ('pressed', input_fg), ]
            }
        },
        'no.TButton': {
            'configure': {
                'padding': (10, 5, 10, 5),
                'background': bg,  # Default background color
                'foreground': fg,  # Default foreground color
                'font': 'Courier 14 bold italic',
                'border': 0,
                'relief': 'flat'
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('readonly', dark),
                               ('disabled', bg),
                               ('pressed', input_bg), ],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('readonly', light),
                               ('disabled', secondary),
                               ('pressed', input_fg), ]
            }
        },
        'TEntry': {
            'configure': {
                'padding': (10, 5, 10, 5),
                'background': bg,  # Default background color
                'foreground': fg,  # Default foreground color
                'font': 'Courier 18 bold italic'
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', secondary)],
                'foreground': [('focus', danger),
                               ('active', primary),
                               ('!disabled', warning)]
            }
        },
        'TLabel': {
            'configure': {
                'padding': (10, 5, 10, 5),
                'background': bg,  # Default background color
                'foreground': fg,  # Default foreground color
                'font': 'Courier 14 bold italic'
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg)],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary)]
            }
        },
        'title.TLabel': {
            'configure': {
                'padding': (10, 5, 10, 5),
                'background': bg,  # Default background color
                'foreground': fg,  # Default foreground color
                'font': 'Courier 20 bold italic'
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg)],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary)]
            }
        },
        'TCheckbox': {
            'configure': {
                'padding': (3, 2, 3, 2),
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg),
                               ('pressed', info),
                               ('selected', select_bg), ],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary),
                               ('pressed', light),
                               ('selected', select_fg)]
            }},
        'TCheckbox.Label': {
            'configure': {
                'padding': (3, 2, 3, 2),
                'font': 'Courier 14 bold italic'
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg),
                               ('pressed', info),
                               ('selected', select_bg), ],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary),
                               ('pressed', light),
                               ('selected', select_fg)]
            }},
        'TRadiobutton.Label': {
            'configure': {
                'padding': (3, 2, 3, 2),
                'font': 'Courier 14 bold italic',
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg),
                               ('pressed', info),
                               ('selected', select_bg), ],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary),
                               ('pressed', light),
                               ('selected', select_fg)]
            }},
        'TRadiobutton': {
            'configure': {
                'padding': (3, 2, 3, 2),
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg),
                               ('pressed', info),
                               ('selected', select_bg), ],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary),
                               ('pressed', light),
                               ('selected', select_fg)]
            }},
        'TScale': {
            'configure': {
                'padding': (3, 2, 3, 2),
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg),
                               ('pressed', info)],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary),
                               ('pressed', light)]
            }},
        'TScrollbar': {
            'configure': {
                'padding': (3, 2, 3, 2),
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg),
                               ('pressed', info)],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary),
                               ('pressed', light), ]
            }},
        'TSpinbox': {
            'configure': {
                'padding': (3, 2, 3, 2),
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg)],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary)]
            }},
        'TProgressbar': {
            'configure': {
                'padding': (3, 2, 3, 2),
            },
            'map': {
                'background': [('active', bg),
                               ('disabled', bg),
                               ('!disabled', dark), ],
                'foreground': [('active', success),
                               ('disabled', fg),
                               ('!disabled', primary)]
            }},
        'TNotebook': {
            'configure': {'padding': (3, 2, 3, 2),
                          'font': 'Courier 14 bold italic',
                          'border': 0,
                          'relief': 'solid',
                          'background': bg,
                          }},
        'TNotebook.Tab': {
            'configure': {
                    'padding': (3, 2, 3, 2),
                    'font': 'Courier 12 italic',
                    'border': 0,
                    'background': bg},
            'map': {'background': [('active', bg),
                                   ('selected', bg),
                                   ('!disabled', bg)],
                    'foreground': [('active', success),
                                   ('!disabled', fg),
                                   ('focus', border)]}},
        'TSeparator': {
            'configure': {
                'padding': (3, 2, 3, 2), 'background': danger
            }},
        'Treeview': {
            'configure': {
                'padding': (3, 2, 3, 2), 'bordercolor': 'border', 'font': 'Courier 12 bold italic'
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg),
                               ('pressed', info),
                               ('selected', select_bg), ],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary),
                               ('pressed', light),
                               ('selected', select_fg)]
            }},
        'Treeview.Heading': {
            'configure': {
                'padding': (3, 2, 3, 2),
                'font': 'Courier 13 italic'
            },
            'map': {
                'background': [('active', bg),
                               ('!disabled', input_bg),
                               ('disabled', bg),
                               ('pressed', info),
                               ('selected', select_bg), ],
                'foreground': [('focus', success),
                               ('active', primary),
                               ('!disabled', fg),
                               ('disabled', secondary),
                               ('pressed', light),
                               ('selected', select_fg)]
            }},
    })


def themeNameStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    themeName = cursor.fetchone()[1]  # select theme name input foreground color
    connect.commit()
    connect.close()


def primaryStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    primary = cursor.fetchone()[2]  # select theme name input foreground color
    connect.commit()
    connect.close()


def secondaryStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    Secondary = cursor.fetchone()[3]  # select theme name input foreground color
    connect.commit()
    connect.close()


def successStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    success = cursor.fetchone()[4]  # select theme name input foreground color
    connect.commit()
    connect.close()


def infoStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    info = cursor.fetchone()[5]  # select theme name input foreground color
    connect.commit()
    connect.close()


def warningStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    warning = cursor.fetchone()[6]  # select theme name input foreground color
    connect.commit()
    connect.close()


def dangerStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    danger = cursor.fetchone()[7]  # select theme name input foreground color
    connect.commit()
    connect.close()


def lightStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    light = cursor.fetchone()[8]  # select theme name input foreground color
    connect.commit()
    connect.close()


def darkStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    dark = cursor.fetchone()[9]  # select theme name input foreground color
    connect.commit()
    connect.close()


def backgroundStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    bg = cursor.fetchone()[10]  # select theme name input foreground color
    connect.commit()
    connect.close()


def foregroundStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    fg = cursor.fetchone()[11]  # select theme name input foreground color
    connect.commit()
    connect.close()


def select_fgStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    select_fg = cursor.fetchone()[12]  # select theme name input foreground color
    connect.commit()
    connect.close()


def select_bgStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    select_bg = cursor.fetchone()[13]  # select theme name input foreground color
    connect.commit()
    connect.close()


def borderStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    border = cursor.fetchone()[14]  # select theme name input foreground color
    connect.commit()
    connect.close()


def input_fgStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    input_fg = cursor.fetchone()[15]  # select theme name input foreground color
    connect.commit()
    connect.close()


def input_bgStyle():
    ThemesName = open('colorSystem.txt', 'r').read()

    connect = sq.connect('ListColor.db')  # connect to database
    cursor = connect.cursor()
    cursor.execute('''SELECT * from ListColor where themesName=?''', (ThemesName,))
    input_bg = cursor.fetchone()[16]  # select theme name input foreground color
    connect.commit()
    connect.close()
