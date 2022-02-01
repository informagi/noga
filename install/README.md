# Dockerized Matomo setup
Configuration for a dockerized Matomo setup using docker-compose. This docker-compose configuration in this repository takes care of your Matomo server (including SSL connections). The only prerequisites are a working installation of [docker-compose](https://docs.docker.com/compose/) and a server that can host your instance of Matomo.

In order to establish a secure connection you require an SSL certificate.

## Installation

Installation of the Matomo server is straightforward with this repository. You simply have to run the install script, which prompts you with a few questions and values, after which Matomo is installed, configured and started.

You will encounter prompts for the following values:

| Prompt              | Description                                                                                                                        | Default      |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Enable SSL?         | Whether to enable SSL access using a signed SSL certificate.                                                                       | Yes          |
| Enable systemd?     | Whether to enable services that archive and backup your installation.                                                              | Yes          |
| Domain name         | The domain name for your Matomo installation, e.g. `matomo.science.ru.nl`.                                                         | -            |
| MySQL user password | The password for the `matomo` user in your MySQL installation.                                                                     | -            |
| MySQL root password | The password for the `root` user in your MySQL installation.                                                                       | -            |
| PHP memory limit    | The amount of memory PHP is allowed to consume. Necessary for the archive job of larger websites.                                  | 1024m        |
| Systemd user        | As which user the systemd services should run, e.g. `core` or `www-data`. Choose a value with write access to the backup location. | Current user |
| Backup directory    | In which directory the backups should be stored, e.g. `/mnt/rot/backups/`. Backups will be stored in subdirectories `YYYY/MM/DD`.  | -            |

### SSL

If you enable SSL in your installation, you need to supply a signed SSL certificate and corresponding private key. These must be stored under the `keys` subdirectory of the installation location, and be named according to the domain name of your installation. For instance, if the provided domain name is `matomo.science.ru.nl`, the SSL certificate must be under `keys/matomo.science.ru.nl.crt`, and the private key must be under `keys/matomo.science.ru.nl.key`.

### Configuration

During the installation process, Matomo will need to be configured. The installer will direct you to the Matomo webpage, where you will complete the [5-minute Matomo installation](https://matomo.org/docs/installation/#the-5-minute-matomo-installation). Your database will automatically be configured correctly, so you do not have to change any values in step 3.

After you complete the standard Matomo installation, go back to the terminal in which you started the installer, and continue the installation process. After doing so, the installer will update the final configuration values, and (if enabled) install the systemd services. Now your Matomo is ready to use!

### Scripts

The `matomo-compose` setup of Matomo contains 6 scripts to help you organise and manage your installation.

* `archive-reports` handles the [auto-archiving](https://matomo.org/docs/setup-auto-archiving/) of your Matomo setup.
* `backup-db` creates a backup of the entire Matomo database.
* `backup-matomo` creates a backup of the Matomo install files.
* `clean-backups` removes all old backups (i.e. older than 7 days) from the backup directory.
* `restore-db` restores a backup of the entire Matomo database.
* `restore-matomo` restores a backup of the Matomo install files.

If the systemd services are enabled in the installation, the following timers will be installed:

* `archive-reports` runs every hour.
* `backup-db` runs every night at 2:00 AM.
* `backup-matomo` runs every night at 4:00 AM.
* `clean-backups` runs every night at 5:00 AM.
