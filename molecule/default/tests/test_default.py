import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    package = host.package('sensu')
    assert package.is_installed
    assert '1.7.0' in package.version


def test_dir_ownership(host):
    assert host.file('/opt/sensu').group == 'sensu'


def test_main_config(host):
    f = host.file('/etc/sensu/config.json')
    assert f.exists
    assert f.is_file
    assert f.user == 'sensu'
    assert f.group == 'sensu'
    assert f.mode == 0o600
    assert f.contains('rabbitmq')
    assert f.contains('check-cpu.rb')
    assert f.contains('"foo": "bar"')
    assert f.contains('example_subscription')
    assert f.contains('"zip": "zap"')
    assert not f.contains('subscription_to_be_overridden')


def test_server_running(host):
    server = host.service('sensu-server')
    assert server.is_running
    assert server.is_enabled


def test_api_running(host):
    api = host.service('sensu-api')
    assert api.is_running
    assert api.is_enabled


def test_client_running(host):
    client = host.service('sensu-client')
    assert client.is_running
    assert client.is_enabled


def test_api_listening(host):
    assert host.socket('tcp://0.0.0.0:4567').is_listening


def test_plugin_installed(host):
    assert host.file('/opt/sensu/embedded/bin/check-memory.rb').exists


# Tests extension install/enable
def test_snmp_listening(host):
    assert host.socket('udp://0.0.0.0:1062').is_listening
