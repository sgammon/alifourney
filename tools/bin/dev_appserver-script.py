#!"C:\Python27\python.exe"

import os

join = os.path.join
base = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
base = os.path.dirname(base)
base = os.path.dirname(base)

import sys
sys.path[0:0] = [
    join(base, 'app'),
    join(base, 'app\\lib'),
    join(base, 'app\\lib\\dist'),
    join(base, 'var\\eggs'),
    join(base, 'var\\develop-eggs'),
    join(base, 'var\\eggs\\appfy.recipe.gae-0.9.3-py2.7.egg'),
    join(base, 'var\\parts\\google_appengine'),
    ]


gae = join(base, 'var\\parts\\google_appengine')
cfg = join(base, 'gaetools.cfg')

import appfy.recipe.gae.scripts

if __name__ == '__main__':
    appfy.recipe.gae.scripts.dev_appserver(base, gae, cfg)
