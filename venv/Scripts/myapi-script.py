#!c:\users\antonio\stack_camp\restful_api\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'myapi','console_scripts','myapi'
__requires__ = 'myapi'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('myapi', 'console_scripts', 'myapi')()
    )
