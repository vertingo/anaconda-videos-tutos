#!C:/Users/tedal/OneDrive/Bureau/Projet Informatique/Anaconda/anaconda-project-master/envs/anaconda-project-dev\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'anaconda-client==1.7.2','console_scripts','conda-server'
__requires__ = 'anaconda-client==1.7.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('anaconda-client==1.7.2', 'console_scripts', 'conda-server')()
    )
