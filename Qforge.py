#!/usr/bin/env python3

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
sorzkode
sorzkode@proton.me
https://github.com/sorzkode

MIT License
Copyright (c) 2022 sorzkode
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

# Left window setup
inputside = [[sg.Image(filename='assets\qflogo.png', key='-LOGO-')],
             [sg.Text('A Python QR Code Generator', font=('Lucida', 10, ITALIC), text_color='Gray', pad=(10,5))],
             [sg.Text('URL:', font=('Lucida', 12, BOLD), pad=(0,5)), sg.In(size=50, font=('Lucida', 11, BOLD), enable_events=True, key='-URL-')],
             [sg.Text('Color:', font=('Lucida', 12, BOLD), pad=(0,0)), sg.Combo(qrcolors, default_value=qrcolors[0], s=(15,22), enable_events=True, readonly=True, k='-COMBO-'), sg.Text('           '), sg.Button('Generate', font=('Lucida', 12, BOLD), pad=(5,15)), sg.Button('Clear', font=('Lucida', 12, BOLD), pad=(5,15)), sg.Button('Exit', font=('Lucida', 12, BOLD), pad=(5,15))],
             [sg.Text('Note: PDF files do not support multiple colors. \n PDFs will default to black regardless of dropdown selection.', font=('Lucida', 10, ITALIC), text_color='Gray', pad=(0,0))]]

# Right window setup
outputside = [[sg.Text('Sample Code:', font=('Lucida', 11, ITALIC), text_color='Yellow', key='-HDING-')],
              [sg.Image(filename='assets\sample.png', key='-QROUT-')],
              [sg.Text('https://sampleurl.com', font=('Lucida', 10, ITALIC), text_color='Gray', key='-QRTXT-')],
              [sg.Text('Save as:', font=('Lucida', 12)), sg.Button('PDF', font=('Lucida', 12, BOLD)), sg.Button('PNG', font=('Lucida', 12, BOLD)), sg.Button('SVG', font=('Lucida', 12, BOLD))]]

# Full window layout
layout = [[sg.Column(inputside, element_justification='r', pad=(0,0), size=(480,280)), sg.VSeperator(), sg.Column(outputside, element_justification='c', pad=(0,0), size=(240,280))]]

# Call window
window = sg.Window('Qforge - QR Code Generator', layout, resizable=True, icon='assets\qic.ico')

# Events loop - da meat and potatoes
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Generate':
        qrcode = segno.make_qr(values['-URL-'])
        qrcode.save('temp.png', scale=5, dark=values['-COMBO-'])
        window['-QROUT-'].update('temp.png')
        window['-QRTXT-'].update(values['-URL-']) 
        window['-HDING-'].update('Your Code:', font=('Lucida', 11, BOLD), text_color='White')
    
    if event == 'Clear':
        window['-URL-'].update('')
        window['-COMBO-'].update(qrcolors[0])
        window['-QROUT-'].update('assets\sample.png')
        window['-QRTXT-'].update('URL cleared') 
        window['-HDING-'].update('Sample Code:', font=('Lucida', 11, ITALIC), text_color='Yellow')

    if event == 'PDF':
        pdflocation = sg.popup_get_folder('Select a Save location')
        pdfname = sg.popup_get_text('What do you want to call your file?')
        pdfcode = segno.make_qr(values['-URL-'])
        pdfcode.save(pdflocation + '/' + pdfname + '.' + 'pdf', scale=10)
        window['-QRTXT-'].update(f'To: {pdflocation}') 
        window['-HDING-'].update('Saved as PDF:', font=('Lucida', 11, ITALIC), text_color='Yellow')
        sg.Popup(f'Saved {pdflocation}/{pdfname}.pdf.')

    if event == 'PNG':
        pnglocation = sg.popup_get_folder('Select a Save location')
        pngname = sg.popup_get_text('What do you want to call your file?')
        pngcode = segno.make_qr(values['-URL-'])
        pngcode.save(pnglocation + '/' + pngname + '.' + 'png', scale=10, dark=values['-COMBO-'])
        window['-QRTXT-'].update(f'To: {pnglocation}') 
        window['-HDING-'].update('Saved as PNG:', font=('Lucida', 11, ITALIC), text_color='Yellow')
        sg.Popup(f'Saved {pnglocation}/{pngname}.png.')

    if event == 'SVG':
        svglocation = sg.popup_get_folder('Select a Save location')
        svgname = sg.popup_get_text('What do you want to call your file?')
        svgcode = segno.make_qr(values['-URL-'])
        svgcode.save(svglocation + '/' + svgname + '.' + 'svg', scale=10, dark=values['-COMBO-'], xmldecl=False, svgns=False, svgclass=None)
        window['-QRTXT-'].update(f'To: {svglocation}') 
        window['-HDING-'].update('Saved as SVG:', font=('Lucida', 11, ITALIC), text_color='Yellow')
        sg.Popup(f'Saved {svglocation}/{svgname}.svg.')

window.close()
