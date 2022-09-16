# killing a process using pkill

exec { 'killmenow':
command  => 'pkill killmenow',
path     => '/usr/bin',
provider => 'shell',
}
