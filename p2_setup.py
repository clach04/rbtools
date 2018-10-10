"""
Issue:

NOTE using Python 2.4, this results in an exe about 4Mb in size.
NOTE using Python 2.6, this results in an exe about 5.5Mb in size.

    E:\Python24\python.exe p2_setup.py py2exe
    c:\python24\python p2_setup.py py2exe
    setup.py py2exe

Quick-N-Dirty create win32 binaries and zip file script.
Zero error checking.

TODO inject 'py2exe' into sys.argv?
"""
import os
import sys
import glob
import shutil

from distutils.core import setup

try:
    import py2exe
except ImportError:
    # either non-Windows or py2exe just not installed
    py2exe = None


# Clean temp Python/Jython files
delete_list = glob.glob('simplejson/*.pyc') + glob.glob('simplejson/*$py.class')
for x in delete_list:
    os.remove(x)

try:
    shutil.rmtree('dist')
except WindowsError, info:
    # assume directory does not exist
    pass

print 'nasty copy hack'
shutil.copy2(os.path.join('rbtools', 'postreview.py'), 'postreview.py')

if len(sys.argv) == 1:
    if py2exe:
        print 'defaulting to creating py2exe'
        sys.argv += ['py2exe']
    else:
        print 'py2exe not available'
        sys.argv += ['sdist']

# disable optimization- we _may_ need docs strings, specifically "copyright"
setup(
    options={"py2exe": {
                            #"includes": ["decimal"],
                            "optimize": 1,  # 1 and NOT 2 because I use the __doc__ string as the usage string. 2 optimises out the doc strings
                            'bundle_files': 1,
                            ## options to reduce size of final exe
                            #~ 'ascii': True,  # Exclude encodings
                            'excludes': [
                                        '_ssl',  # Exclude _ssl
                                        'pyreadline',  # 'difflib', 
                                        'doctest',  # 'locale',
                                        #'optparse', 
                                        'pickle',  # 'calendar',# Exclude standard library
                                        #'re',
                                        ],  
                            }
            },
    zipfile=None,  # try and make a single exe, if do not want this loose this and the 'bundle_files' option
    console=['postreview.py']
    )

zipfilename = 'distribute_me.zip'
zipfilelist = ['p2_readme.txt', '__main__.py', 'postreview.py', os.path.join('win32bin', 'diff.exe'), os.path.join('win32bin', 'p.exe')] + glob.glob('rbtools/*.py') + glob.glob('rbtools/*/*.py') + glob.glob('simplejson/*') + glob.glob('dist/*')

import zipfile
z = zipfile.ZipFile(zipfilename, 'w')
for x in zipfilelist:
    z.write(x)
z.close()

print 'Created:', zipfilename
