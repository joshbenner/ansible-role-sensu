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
| `sensu_config`              | Config tree for main config file. Override specific settings instead. |
| `sensu_transport_name`      | Which transport Sensu should use (`rabbitmq` or `redis`).             |
| `sensu_rabbitmq_config`     | RabbitMQ configuration scope.                                         |
| `sensu_redis_config`        | Redis configuration scope.                                            |
| `sensu_api_config`          | API configuration scope.                                              |
| `sensu_client_config`       | Client configuration scope.                                           |
| `sensu_pin_version`         | Whether to pin a specific version (depends on `sensu_version`)        |
| `sensu_install_yum_versionlock` | Whether to install YUM versionlock plugin. Required if pinning.   |

Merged Configurations
---------------------

The role will merge variables with specific suffixes to assemble configurations for things like checks from multiple sources without needing Ansible merging enabled.

For instance, if you have vars in `group_vars/all`:

```yml
base_sensu_checks:
  check_memory:
    command: check-memory-percent.rb -w 70 -c 80
    interval: 60
    standalone: true
  check_swap:
    command: check-swap-percent.rb -w 50 -c 80
    interval: 60
    standalone: true
```

and in `group_vars/rabbit-servers`:

```yaml
rabbitmq_sensu_checks:
  check_rabbitmq_alive:
    command: check-rabbitmq-amqp-alive.rb
    interval: 60
    standalone: true
```

Then on a server in the `rabbit-servers` group, the checks will be combined to result in a configuration like:

```yaml
sensu_checks:
  check_memory:
    command: check-memory-percent.rb -w 70 -c 80
    interval: 60
    standalone: true
  check_swap:
    command: check-swap-percent.rb -w 50 -c 80
    interval: 60
    standalone: true
  check_rabbitmq_alive:
    command: check-rabbitmq-amqp-alive.rb
    interval: 60
    standalone: true
```

The following suffixes are merged for Sensu configurations:

* `_sensu_checks` - Sensu check definitions
* `_sensu_handlers` - Sensu handler definitions
* `_sensu_filters` - Sensu filter definitions
* `_sensu_mutators` - Sensu mutator definitions
* `_sensu_plugins` - Sensu plugins to install, as a string name, or object with more detail:

    ```yml
    some_prefix__sensu_plugins:
      - name: pagerduty
        version: 3.0.1
    ```

* `_sensu_plugin_dependencies`

Example Playbook
----------------

```yaml
- hosts: all
  become: yes
  roles:
    - role: joshbenner.rabbitmq
    - role: DavidWittman.redis
    - role: joshbenner.sensu
      sensu_enable_server: yes
      sensu_enable_api: yes
      my_sensu_plugins:
        - cpu-checks
        - memory-checks
        - network-checks
        - rabbitmq
        - redis
      my_sensu_checks:
        check_cpu:
          command: check-cpu.rb -w 80 -c 95
          interval: 60
          standalone: true
        check_memory:
          command: check-memory-percent.rb -w 70 -c 80
          interval: 60
          standalone: true
        check_swap:
          command: check-swap-percent.rb -w 50 -c 80
          interval: 60
          standalone: true
        check_route:
          command: check-ping.rb -h {{ ansible_default_ipv4.gateway }} -W 90 -C 50
          interval: 60
          standalone: true
        check_rabbitmq_alive:
          command: check-rabbitmq-amqp-alive.rb
          interval: 60
          standalone: true
        check_redis_alive:
          command: check-redis-ping.rb
          interval: 60
          standalone: true
```

License
-------

BSD
