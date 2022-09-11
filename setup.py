import setuptools

setuptools.setup(
    name='Qforge',
    version='1.0.0',
    description='QR Code Generator.',
    url='https://github.com/sorzkode/',
    author='sorzkode',
    author_email='<sorzkode@proton.me>',
    packages=setuptools.find_packages(),
    install_requires=['segno', 'PySimpleGUI'],
    long_description='A Python QR Code Generator made with PySimpleGUI and sgeno.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT',
        'Operating System :: OS Independent',
        ],
)