Sensu
=====

[![Build Status](https://travis-ci.org/joshbenner/ansible-role-sensu.svg?branch=master)](https://travis-ci.org/joshbenner/ansible-role-sensu)

Install and configure sensu core (community version).

Role Variables
--------------
Available variables listed below. For defaults, see `defaults/main.yml`.

| Variable                    | Description                                                           |
|-----------------------------|-----------------------------------------------------------------------|
| `sensu_install_repo`        | Whether to install the custom Debian repo.                            |
| `sensu_debian_repo_key_url` | URL to the Debian repository GPG key.                                 |
| `sensu_debian_repo_url`     | URL of the Debian repo to use.                                        |
| `sensu_redhat_repo_url`     | Url of the RedHat repo to use.                                        |
| `sensu_state`               | The install state of sensu (ie: present/absent).                      |
| `sensu_version`             | Specific version of Sensu to install.                                 |
| `sensu_user`                | The Sensu user.                                                       |
| `sensu_group`               | The Sensu group.                                                      |
| `sensu_config_file`         | Path to main Sensu configuration file.                                |
| `sensu_config_dir`          | Path to directory containing additional Sensu confs.                  |
| `sensu_enable_server`       | Whether to run the server.                                            |
| `sensu_enable_api`          | Whether to run the API.                                               |
| `sensu_enable_client`       | Whether to run the client.                                            |
| `sensu_plugin_dependencies` | The list of packages to install to support plugins.                   |
| `sensu_config`              | Config tree for main config file. Override specific settings instead. |
| `sensu_transport_name`      | Which transport Sensu should use (`rabbitmq` or `redis`).             |
| `sensu_rabbitmq_config`     | RabbitMQ configuration scope.                                         |
| `sensu_redis_config`        | Redis configuration scope.                                            |
| `sensu_api_config`          | API configuration scope.                                              |
| `sensu_client_config`       | Client configuration scope.                                           |
|                             |                                                                       |

License
-------

BSD
