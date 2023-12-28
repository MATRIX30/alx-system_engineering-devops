# Using Puppet, install flask from pip3.

#  Requirements:

#   Install flask
#   Version must be 2.1.0
# package {'python3.8':

# ensure => '3.8.10',

# }

# 

# package {'python3-pip':

# ensure => installed,

# require => Package['python3.8'],

# }

# package { 'Werkzeug':

# ensure => '2.1.1',

# require => Package['python3.8'],

# }
# package {'flask':

# ensure => '2.1.0',

# provider => 'pip3',

# # require => Package['python3.8','python3-pip', 'Werkzeug'],

# }

exec {'flask-install':
  command => 'pip3 install flask==2.1.0',
  path    => '/usr/bin'
}
