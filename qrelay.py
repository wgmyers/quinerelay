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
chomp ($q, $r);
printf $r,($p,$p2,$p2,$q,$p2,$p2,$r,$p2);
print $/;"""
r = """#!/usr/bin/env python
p = '%s'
p2 = '%s'
q = %s%s%s
r = %s%s%s
print q %% (p, p2, p, q, p, p, r, p)"""
print q % (p, p2, p, q, p, p, r, p)
