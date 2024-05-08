# Fixes getting permissions on wordpress site

$uploads_dir = '/var/www/html/wp-content/uploads'

file { $uploads_dir:
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

exec { 'fix-wp-uploads-permissions':
  command => "chmod -R u=rwX,go=rX ${uploads_dir}",
  path    => '/bin:/usr/bin',
  onlyif  => "test -d ${uploads_dir}",
  require => File[$uploads_dir],
}
