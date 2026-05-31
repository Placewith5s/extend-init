import sys
import atexit

from extend_init.modules.frontend_template import *
from extend_init.modules.empty_folders import ask_common_vanilla_frontend
from extend_init.modules.empty_files import ask_gh_pages


def main():
    print("Platform code:", sys.platform)
    print("\n")

    if sys.platform == "win32":
        print("Windows is not supported!")
        sys.exit(0)

    ask_frontend_template()
    ask_common_vanilla_frontend()
    ask_gh_pages()


if __name__ == '__main__':
    main()


@atexit.register
def program_exit():
    print("Exited program")
