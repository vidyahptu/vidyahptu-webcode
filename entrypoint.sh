#!/bin/bash

# Clone the repository, checkout 'for_server', and run Composer install
cd mainweb
composer install

#run the file
php artisan serve --host=0.0.0.0 --port=8000 &
# Start a long-running process to keep the container running
tail -f /dev/null