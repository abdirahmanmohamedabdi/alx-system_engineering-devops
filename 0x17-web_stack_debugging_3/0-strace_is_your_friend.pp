# setting fixed at wordpress
exec { 'settingsPress':
  command => 'sed -i "s/\b.phpp\b/.php/g" /var/www/html/wp-settings.php'
  provider => shell,
}
