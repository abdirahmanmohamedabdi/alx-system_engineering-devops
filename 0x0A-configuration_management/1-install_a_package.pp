#!/usr/bin/pup
#Install an especific bersion of flask (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}