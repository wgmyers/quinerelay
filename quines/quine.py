#!/usr/bin/env python
p = '"""'
q = """#!/usr/bin/env python
p = '%s'
q = %s%s%s
print q %% (p, p, q, p)"""
print q % (p, p, q, p)
