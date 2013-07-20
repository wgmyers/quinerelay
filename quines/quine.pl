#!/usr/bin/perl
$p='HERE';
$q=<<'HERE';
#!/usr/bin/perl
$p='%s';
$q=<<'%s';
%s%s
printf $q,($p,$p,$q,$p);
HERE
printf $q,($p,$p,$q,$p);
