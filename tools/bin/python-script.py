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

_interactive = True
if len(sys.argv) > 1:
    _options, _args = __import__("getopt").getopt(sys.argv[1:], 'ic:m:')
    _interactive = False
    for (_opt, _val) in _options:
        if _opt == '-i':
            _interactive = True
        elif _opt == '-c':
            exec _val
        elif _opt == '-m':
            sys.argv[1:] = _args
            _args = []
            __import__("runpy").run_module(
                 _val, {}, "__main__", alter_sys=True)

    if _args:
        sys.argv[:] = _args
        __file__ = _args[0]
        del _options, _args
        execfile(__file__)

if _interactive:
    del _interactive
    __import__("code").interact(banner="", local=globals())
