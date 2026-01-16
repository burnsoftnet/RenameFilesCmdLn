# RenameFilesCmdLn

Command line python script that will help you rename all the files in a directory and keep the extension

Original Build to help categorize image files but can be used for everything you need to rename.

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=JSW8XEMQVH4BE)]

## Requirements

* Windows 10 or 11, macOS, or linux Machine
* Python 3.11

## SetUp Script

There is a setup script that you can use to help create a python virtual environment and install all the required libraries to 
run the script or compile into an executable.

Once you have the repo downloaded, open a command line, goto the directory of the repo and run the setup script
If you want to setup a virtual environment.  

For the most part the required libraries that is installed in the virtual Environment
for making an executable.  If you just want to rename thing from the source directory just run the script.

```
python setup.py
```

## Creating the EXE

This is optional if you want to run the python script as an executable or if you want to run the script on its own.
Once you run the setup script you can run the command in the virtual environment to compile the app by just using the 
command below

### SAMPLE

```commandline
pyinstaller -F --paths=<Path to site-packages> RenameFiles.py
```

### EXAMPLE Window

```commandline
pyinstaller -F --paths=C:\Software\RenameFilesCmdLn\venv\Lib\site-packages RenameFiles.py
```

### EXAMPLE Mac OS

```commandline
pyinstaller -F --paths=/Users/test/Documents/Source_Code/Scripting/PycharmProjects/RenameFilesCmdLn/venv/Lib/site-packages RenameFiles.py
```

## Running the Script Only

If you didn't want to create an executable and just wanted to run the script or if there was issues when creating the executable.
You can run the command below to 

### SAMPLE

```commandline
python.exe RenameFiles.py --dir="<DIRECTORY OF TARGET FILES>" --name="<NEW NAME>"
```

### SAMPLE Replace Original Name

Replace the original name with the new one plus a number, EXAMPLE: testname_00001.jpg

```commandline
python.exe RenameFiles.py --dir="/Users/test/Downloads/test" --name="Test"
```

### SAMPLE Append new to old Original Name

Append the new name to the original, EXAMPLE: testname_old_name.jpg

```commandline
python.exe RenameFiles.py --dir="/Users/test/Downloads/test" --name="Test"  --keeporgname=True
```

## Change Log

## v0.0.1

* Init Release