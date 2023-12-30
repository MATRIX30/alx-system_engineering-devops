$ssh_config_content = @(EOT)
Host *
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no
EOT

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  content => $ssh_config_content,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
}
