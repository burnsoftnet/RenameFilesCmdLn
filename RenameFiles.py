from renamefiles import application
from sys import platform
import multiprocessing

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if platform == 'darwin':
        multiprocessing.set_start_method("spawn")
    app = application.Application()
    app.main()

