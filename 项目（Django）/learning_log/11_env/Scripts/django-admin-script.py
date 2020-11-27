#!h:\python\实例代码\alieninvasion\项目（django）\learning_log\11_env\scripts\python.exe -x
# EASY-INSTALL-ENTRY-SCRIPT: 'Django==3.1.3','console_scripts','django-admin'
__requires__ = 'Django==3.1.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Django==3.1.3', 'console_scripts', 'django-admin')()
    )
