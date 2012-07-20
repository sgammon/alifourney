#!"C:\Python27\python.exe" -S

import os

join = os.path.join
base = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
base = os.path.dirname(base)
base = os.path.dirname(base)

import sys
sys.path[0:0] = [
    join(base, 'var\\parts\\buildout'),
    ]


import os
path = sys.path[0]
if os.environ.get('PYTHONPATH'):
    path = os.pathsep.join([path, os.environ['PYTHONPATH']])
os.environ['BUILDOUT_ORIGINAL_PYTHONPATH'] = os.environ.get('PYTHONPATH', '')
os.environ['PYTHONPATH'] = path
import site # imports custom buildout-generated site.py

import zc.buildout.buildout

if __name__ == '__main__':
    zc.buildout.buildout.main()
