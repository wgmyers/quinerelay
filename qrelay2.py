#!/usr/bin/env python
p = 'HERE'
p2 = '"""'
q = """#!/usr/bin/perl
$p='%s';
$p2='%s';
$q=<<'%s';
%s
%s
$r=<<'%s';
%s
%s
$s=<<'%s';
%s
%s
chomp ($q, $r, $s);
printf $r,($p,$p2,$p2,$q,$p2,$p2,$r,$p2,$p2,$s,$p2,$p2);
print $/;
"""
r = """#!/usr/bin/env python
p = '%s'
p2 = '%s'
q = %s%s
%s
r = %s%s
%s
s = %s%s
%s
print s %% (p, p2, p, q, p, p, r, p, p, s, p)
"""
s = """#!/usr/bin/env ruby
p='%s'
p2='%s'
q=<<%s
%s%s
r=<<%s
%s%s
s=<<%s
%s%s
q.chomp!
r.chomp!
s.chomp!
printf(q,p,p2,p,q,p,p,r,p,p,s,p)
puts
"""
print s % (p, p2, p, q, p, p, r, p, p, s, p)
