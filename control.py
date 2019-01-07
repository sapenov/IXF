# THE CONTROL PART

import IXFParser.py

in = '/tmp/export.ixf'
out = '/tmp/out.json'

r = new IXFParser()
r.process(in, out)
