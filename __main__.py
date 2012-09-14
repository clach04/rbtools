#!/usr/bin/env python
# -*- coding: us-ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
"""Dumb wrapper script to allow postreview to be invoked from a zip file.

Example:

    python zip_file_where_this_is_in_the_root.zip

"""

import os
import sys

import rbtools
import rbtools.postreview


def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    rbtools.postreview.main()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
