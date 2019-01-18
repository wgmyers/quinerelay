#!/usr/bin/env ruby
p='HERE'
q=<<HERE
#!/usr/bin/env ruby
p='%s'
q=<<%s
%s%s
printf(q,p,p,q,p)
HERE
printf(q,p,p,q,p)
