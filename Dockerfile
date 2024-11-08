

FROM ubuntu:latest

# Set the DEBIAN_FRONTEND to noninteractive to prevent interactive prompts

ENV DEBIAN_FRONTEND=noninteractive


# Update package lists and install required packages
RUN apt-get update
RUN apt-get install -y git 
RUN apt-get install -y php

# Install additional PHP packages
RUN apt-get install -y php-dom php-xml php-curl

# Install zip and unzip
RUN apt-get install -y zip unzip
RUN apt-get install -y php-sqlite3

# Install zip and unzip

# Download and install Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && rm composer-setup.php

RUN apt-get install -y php-mysql

##inslling python
#RUN apt-get install -y python3
##inslin pip3
#RUN apt-get  install -y python3-pip

#RUN pip install pymongo
#RUN pip install requests
# Set the working directory
WORKDIR /app

# Define the entry point script
COPY mainweb /app/
COPY entrypoint.sh /app/entrypoint.sh

# Make the entry point script executable
RUN chmod +x /app/entrypoint.sh

# Define the main command to run when the container starts
CMD ["/app/entrypoint.sh"]