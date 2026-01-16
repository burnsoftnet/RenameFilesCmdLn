"""
Setup script to help create the virtual environment for this repository is needed and install the
required libraries for this robot test.  Most information in this script should be plug and play.
If there are any libraries you want to install from disk, put it in the requirements.txt file.  If
the requirements.txt does not exist, it will skip over it.

The python for Windows should be the same no matter what, the linux command can vary, so verify the command
on the target linux before running the script.  If it is different from python3, please update the script
before running.
"""
__author__ = 'Joe Mireles'
__copyright__ = 'Copyright © www.burnsoft.net 2022'
__version__ = '1.0.2'
__maintainer__ = 'Joe Mireles'
__status__ = 'Release'
"""The status of the Script if it is in Release or in Development mode.  Development Mode has more 
output while viewing the script
"""

import os
import shutil

virtualEnvironmentFolderName = "venv"
rootPath = os.path.join(os.path.dirname(os.path.abspath(__file__)))
virtualEnvironmentPath = os.path.join(rootPath, virtualEnvironmentFolderName)
RequirementsPath = os.path.join(rootPath, "requirements.txt")

if os.path.exists(virtualEnvironmentPath):
    print("Deleting old virtualenv")
    shutil.rmtree(virtualEnvironmentPath)

print("")
print("====================================================================================================")
print("Starting Setup for project {} Python Robot Tests".format(os.path.basename(rootPath)))
print("{}".format(__copyright__))
print("Version: {} ({})".format(__version__, __status__))
print("====================================================================================================")

# region "Settings for either windows or linux / macOS"
if os.name == 'nt':
    pyCmd = "python"
    virtualEnvironmentScriptsPath = os.path.join(virtualEnvironmentPath, "scripts")
    virtualEnvironmentPythonCommandPath = os.path.join(virtualEnvironmentScriptsPath, pyCmd)
    ActivateVirtualEnvironmentCommand = ".\\{}\\Scripts\\activate".format(virtualEnvironmentFolderName)
    ActivePythonWhereCommand = "where python"
    ShowInstalledPackages = "{} -m pip freeze".format(virtualEnvironmentPythonCommandPath)
else:
    pyCmd = "python3"
    virtualEnvironmentScriptsPath = os.path.join(virtualEnvironmentPath, "bin")
    virtualEnvironmentPythonCommandPath = os.path.join(virtualEnvironmentScriptsPath, pyCmd)
    ActivateVirtualEnvironmentCommand = "source {}/bin/activate".format(virtualEnvironmentFolderName)
    ActivePythonWhereCommand = "which python"
    ShowInstalledPackages = "{} -m pip freeze".format(virtualEnvironmentPythonCommandPath)
# endregion

# region "Setup Virtual Environments and upgrade pip"
if os.path.exists(RequirementsPath):
    os.system(f"{pyCmd} -m pip install --upgrade pip")

if not os.path.exists(virtualEnvironmentPath):
    os.system("{} -m venv {}".format(pyCmd, virtualEnvironmentFolderName))
# endregion

# region "Install Packages"

if os.path.exists(RequirementsPath):
    os.system("{} -m pip install -r {}".format(virtualEnvironmentPythonCommandPath, RequirementsPath))

if __status__.lower() == "development":
    os.system(ShowInstalledPackages)


# endregion
print("")
print("")
print("====================================================================================================")
print("Setup is complete, please run Robot Tests from Virtual Directory: {}".format(virtualEnvironmentPath))
print("Or Activate virtual environment by using the command below:")
print(ActivateVirtualEnvironmentCommand)
print("====================================================================================================")
