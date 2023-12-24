import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='Qforge',
    version='1.1.0',
    description='QR Code Generator.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sorzkode/',
    author='Mister Riley',
    author_email='<sorzkode@proton.me>',
    packages=setuptools.find_packages(),
    install_requires=['segno', 'PySimpleGUI', 'tkinter'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
