# making sure nginx is installed
package { 'nginx':
  ensure => 'installed',
}

# Creating dirs if they don't exist
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
}

# Creating a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html><body>Test HTML Page</body></html>',
}

# Creating symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

# Recursive ownership recursively
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  recurse => true,
}

# Updating Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => template('nginx_config.erb'),
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
