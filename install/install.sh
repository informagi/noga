#!/bin/bash

DRY_RUN=false

set -e
install_dir="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Check if docker-compose is installed. If not, we can abort immediately
docker-compose --version > /dev/null 2>&1 || (echo "Could not run docker-compose, which is necessary for this Matomo installation..."; exit 1)

prompt_boolean() {
    # Prompts the user for a boolean y/n, and stores it as either true or false in the second argument.

    local -n result=$2

    read -p "$1 [Y/n] " -n 1 -r value
    [[ -z "$value" ]] || echo

    if [[ $value =~ ^[Nn]$ ]] ; then
        result=false
    else
        result=true
    fi
}

install_matomo() {
    # Installs Matomo by requesting the relevant values from the user and generating the correct config files.
    # After installation, Matomo is started and the user is asked to finish setup in the browser.

    read -p "Enter the domain name of your Matomo installation: " matomo_domain_name
    read -p "Enter your MySQL user password: " mysql_user_password
    read -p "Enter your MySQL root password: " mysql_root_password
    export matomo_domain_name mysql_user_password mysql_root_password


    if [[ $enable_ssl == true ]] ; then
        ssl_dir="${install_dir}/templates"
        matomo_url="https://${matomo_domain_name}"
    else
        ssl_dir="${install_dir}/templates/nossl"
        matomo_url="http://${matomo_domain_name}"
    fi

    if [[ $DRY_RUN == true ]] ; then
        echo "Installing Matomo with:"
        echo "  matomo_domain_name: $matomo_domain_name"
        echo "  mysql_user_password: $mysql_user_password"
        echo "  mysql_root_password: $mysql_root_password"
        echo "  SSL enabled: $enable_ssl"
        echo "  systemd enabled: $enable_systemd"
        echo
        return
    fi

    format='$matomo_domain_name,$mysql_user_password,$mysql_root_password'
    envsubst "$format" < "${ssl_dir}/docker-compose.yml"         > "${install_dir}/docker-compose.yml"
    envsubst "$format" < "${ssl_dir}/nginx.conf"                 > "${install_dir}/conf/nginx.conf"
    envsubst "$format" < "${install_dir}/templates/db.env"       > "${install_dir}/conf/db.env"
    envsubst "$format" < "${install_dir}/templates/db.env"       > "${install_dir}/conf/db.env"
    envsubst "$format" < "${install_dir}/templates/in-file.cnf"  > "${install_dir}/conf/in-file.cnf"
    envsubst "$format" < "${install_dir}/templates/setup-db.sql" > "${install_dir}/conf/setup-db.sql"

    # Ensure SELinux permissions are set correctly.
    # If not, the Docker containers will not have permissions to access the files
    # in the volumes, and they will not be able to start.
    mkdir -p "${install_dir}/setup"
    sudo chcon -Rt svirt_sandbox_file_t "${install_dir}/conf"
    sudo chcon -Rt svirt_sandbox_file_t "${install_dir}/setup"

    echo "Starting Matomo..."
    cd $install_dir && docker-compose up -d

    echo "Please visit ${matomo_url} to complete the Matomo installation."
    read -p "After finishing the installation, press ENTER to continue."
}

configure_matomo() {
    # Configures Matomo by inserting the correct config values in config/config.ini.php.
    # Also ensures the PHP configuration is correctly set.

    configs=(
        'log.log_writers[]="file"'
        'General.datatable_archiving_maximum_rows_actions=5000000'
        'General.datatable_archiving_maximum_rows_events=5000000'
        'General.datatable_archiving_maximum_rows_subtable_actions=5000000'
        'General.datatable_archiving_maximum_rows_subtable_events=1000000'
        'General.minimum_memory_limit_when_archiving=-1'
        'General.proxy_client_headers[]="HTTP_X_FORWARDED_FOR"'
        'General.proxy_host_headers[]="HTTP_X_FORWARDED_HOST"'
    )

    if [[ $enable_ssl == true ]] ; then
        configs+=(
            'General.force_ssl=1'
            'General.assume_secure_protocol=1'
        )
    fi

    read -p "How much memory should PHP be allowed to use? [1024m] " php_mem_limit
    if [[ -z "$php_mem_limit" ]] ; then
        php_mem_limit='1024m'
    fi

    if [[ $DRY_RUN == true ]] ; then
        echo "Adding configuration settings:"

        for conf in ${configs[@]} ; do
            echo "  $conf"
        done

        echo "Adding line to php.ini:"
        echo "  memory_limit=$php_mem_limit"
        echo
        return
    fi

    for conf in ${configs[@]} ; do
        docker exec matomo_app bash -c "/var/www/html/console config:set '$conf'"
    done

    docker exec matomo_app bash -c "echo 'memory_limit=$php_mem_limit' >> /usr/local/etc/php/conf.d/php-matomo.ini"
}

install_systemd_services() {
    current_user=$(whoami)
    read -p "As which user should the systemd services run? [$current_user] " response
    if [[ -z "$response" ]] ; then
        export systemd_user=$current_user
    else
        export systemd_user=$response
    fi

    read -p "In which directory should backups be stored? " backup_dir

    export scripts_dir="${install_dir}/scripts" backup_dir install_dir
    format='$systemd_user$scripts_dir$backup_dir$matomo_domain_name$install_dir'

    for file in ${install_dir}/templates/services/* ; do
        filename=$(basename $file)
        dest="/etc/systemd/system/$filename"

        if [[ $DRY_RUN == true ]] ; then
            echo "Moved $filename to $dest"
        else
            envsubst "$format" < "$file" | sudo tee "$dest" > /dev/null
        fi
    done

    for file in ${install_dir}/templates/services/*.service ; do
        service=$(basename $file)
        if [[ $DRY_RUN == true ]] ; then
            echo "Enabling $service"
        else
            sudo systemctl enable "$service"
        fi
    done
}

prompt_boolean "Do you want to enable SSL?" enable_ssl
prompt_boolean "Do you want to enable systemd services for archiving and backups?" enable_systemd

echo "Installing Matomo..."
install_matomo

echo "Configuring Matomo..."
configure_matomo

if [[ $enable_systemd == true ]] ; then
    echo "Installing systemd services..."
    install_systemd_services
fi
