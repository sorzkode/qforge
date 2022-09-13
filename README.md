[![CodeQL](https://github.com/sorzkode/qforge/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/sorzkode/qforge/actions/workflows/codeql-analysis.yml)
[[MIT Licence](https://en.wikipedia.org/wiki/MIT_License)]


![alt text](https://raw.githubusercontent.com/sorzkode/qforge/master/assets/qforgegit.png)

# Qforge

A Python QR Code Generator using PySimpleGUI and segno.

## Example

![alt text](https://raw.githubusercontent.com/sorzkode/qforge/master/assets/example.png)

## Installation

Download from Github, changedir (cd) to the script directory and run the following:
```
pip install -e .
```
*This will install the qforge package locally 

Installation isn't required to run the script but you will need to ensure the requirements below are met.

## Requirements

  [[Python 3](https://www.python.org/downloads/)]

  [[PySimpleGUI module](https://pypi.org/project/PySimpleGUI/)]

  [[segno module](https://pypi.org/project/segno/)]

  [[tkinter](https://docs.python.org/3/library/tkinter.html)] :: Linux Users

## Usage

If Qforge is installed you can use the following command syntax:
```
python -m Qforge
```
Otherwise you can run the script directly by changing directory (cd) in a terminal of your choice to the Qforge directory and using the following syntax:
```
python Qforge.py
```
Once the script is initiated: 
```
  1. Enter your URL in the inputbox IE https://github.com/sorzkode
  2. Click "Generate" button
  3. Save your file using one of the file format buttons (PDF, PNG, SVG)
  4. Follow prompts
```





