# create a manifest that kills "killmenow"
exec { 'killmenow':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'pkill killmenow',
  provider => 'shell'
}
