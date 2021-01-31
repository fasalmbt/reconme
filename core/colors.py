import sys

colors = True
machine = sys.platform 
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False 
if not colors:
    green =  ''
else:
    green = '\033[92m'