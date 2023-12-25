# Using Puppet, create a file in /tmp.
# Requirements:
#	File path is /tmp/school
#	File permission is 0744
#	File owner is www-data
#	File group is www-data
#	File contains I love Puppet

file { 'file_in_tmp':
    ensure  => file,
    path    => '/tmp/school',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
    mode    => '0744'
}