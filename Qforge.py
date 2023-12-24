#!/usr/bin/env python3
#%%
'''
 ██████  ███████  ██████  ██████   ██████  ███████ 
██    ██ ██      ██    ██ ██   ██ ██       ██      
██    ██ █████   ██    ██ ██████  ██   ███ █████   
██ ▄▄ ██ ██      ██    ██ ██   ██ ██    ██ ██      
 ██████  ██       ██████  ██   ██  ██████  ███████ 
    ▀▀                                             
                                                   
A Python QR Code generator made with PySimpleGUI and segno.
-
Author:
Mister Riley
sorzkode@proton.me
https://github.com/sorzkode

MIT License
Copyright (c) 2024 Mister Riley
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# Dependencies
from tkinter.font import ITALIC, BOLD
import PySimpleGUI as sg
import segno 

# Window theme
sg.theme('DarkTeal9')

# Colors list for combobox
qrcolors = ['Black', 'Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Teal', 'Magenta']

# Fonts
font_subtext = ('Lucida', 10, ITALIC)
font_itl = ('Lucida', 11, ITALIC)
font_title = ('Lucida', 12, BOLD)
font_boldtext = ('Lucida', 11, BOLD)

# Left window setup
inputside = [
    [
        sg.Image(filename='assets\qflogo.png', key='-logo-')
    ],
    [
        sg.Text('A Python QR Code Generator', font=font_subtext, text_color='Gray', pad=(10,5))
    ],
    [
        sg.Text('URL:', font=font_title, pad=(0,5)),
        sg.In(size=50, font=font_boldtext, enable_events=True, key='-url-')
    ],
    [
        sg.Text('Color:', font=font_title, pad=(0,0)),
        sg.Combo(qrcolors, default_value=qrcolors[0], size=(15,22), enable_events=True, readonly=True, key='-combo-'),
        sg.Text('           '),
        sg.Button('Generate', font=font_title, pad=(5,15)),
        sg.Button('Clear', font=font_title, pad=(5,15)),
        sg.Button('Exit', font=font_title, pad=(5,15))
    ],
    [
        sg.Text('Note: PDF files do not support multiple colors. \n PDFs will default to black regardless of dropdown selection.', font=font_subtext, text_color='Gray', pad=(0,0))
    ]
]

# Right window setup
outputside = [
    [
        sg.Text('Sample Code:', font=font_itl, text_color='Yellow', key='-hding-')
    ],
    [
        sg.Image(filename='assets\sample.png', key='-qrout-')
    ],
    [
        sg.Text('https://sampleurl.com', font=font_subtext, text_color='Gray', key='-qrtxt-')
    ],
    [
        sg.Text('Save as:', font=font_title), 
        sg.Button('PDF', font=font_title),
        sg.Button('PNG', font=font_title),
        sg.Button('SVG', font=font_title)
    ]
]

# Full window layout
layout = [
    [sg.Column(inputside, element_justification='r', pad=(0,0)), sg.VSeperator(), sg.Column(outputside, element_justification='c', pad=(0,0))]
]

# Call window
window = sg.Window('Qforge - QR Code Generator', layout, resizable=True, icon='assets\qic.ico')

# Events loop - da meat and potatoes
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Generate':
        try:
            qrcode = segno.make_qr(values['-url-'])
            qrcode.save('temp.png', scale=5, dark=values['-combo-'])
            window['-qrout-'].update('temp.png')
            window['-qrtxt-'].update(values['-url-']) 
            window['-hding-'].update('Your Code:', font=font_boldtext, text_color='White')
        except Exception as e:
            sg.Popup(f'Error generating QR code: {str(e)}')

    if event == 'Clear':
        window['-url-'].update('')
        window['-combo-'].update(qrcolors[0])
        window['-qrout-'].update('assets\sample.png')
        window['-qrtxt-'].update('URL cleared') 
        window['-hding-'].update('Sample Code:', font=font_itl, text_color='Yellow')

    if event == 'PDF':
        try:
            pdflocation = sg.popup_get_folder('Select a Save location')
            pdfname = sg.popup_get_text('What do you want to call your file?')
            pdfcode = segno.make_qr(values['-url-'])
            pdfcode.save(pdflocation + '/' + pdfname + '.' + 'pdf', scale=10)
            window['-qrtxt-'].update(f'To: {pdflocation}') 
            window['-hding-'].update('Saved as PDF:', font=font_itl, text_color='Yellow')
            sg.Popup(f'Saved {pdflocation}/{pdfname}.pdf.')
        except Exception as e:
            sg.Popup(f'Error saving as PDF: {str(e)}')

    if event == 'PNG':
        try:
            pnglocation = sg.popup_get_folder('Select a Save location')
            pngname = sg.popup_get_text('What do you want to call your file?')
            pngcode = segno.make_qr(values['-url-'])
            pngcode.save(pnglocation + '/' + pngname + '.' + 'png', scale=10, dark=values['-combo-'])
            window['-qrtxt-'].update(f'To: {pnglocation}') 
            window['-hding-'].update('Saved as PNG:', font=font_itl, text_color='Yellow')
            sg.Popup(f'Saved {pnglocation}/{pngname}.png.')
        except Exception as e:
            sg.Popup(f'Error saving as PNG: {str(e)}')

    if event == 'SVG':
        try:
            svglocation = sg.popup_get_folder('Select a Save location')
            svgname = sg.popup_get_text('What do you want to call your file?')
            svgcode = segno.make_qr(values['-url-'])
            svgcode.save(svglocation + '/' + svgname + '.' + 'svg', scale=10, dark=values['-combo-'], xmldecl=False, svgns=False, svgclass=None)
            window['-qrtxt-'].update(f'To: {svglocation}') 
            window['-hding-'].update('Saved as SVG:', font=font_itl, text_color='Yellow')
            sg.Popup(f'Saved {svglocation}/{svgname}.svg.')
        except Exception as e:
            sg.Popup(f'Error saving as SVG: {str(e)}')

window.close()
