import i6


def test_container_dockerfile_cwd():
    i6.container().run()

def test_container_docker_hub():
    centos = i6.container({
        'name': 'centos',
        'image': 'centos:latest',
    })
    centos.run()

def test_container_all_options():
    all_config_options = i6.container({
        'name': 'all_config_options',
        'image': 'centos:latest',
        'remove': True,
        'restart': False,
        'ports': {
            '80/tcp': ('0.0.0.0', 8080),
        },
        'volumes': {
            'db': {'bind': '/var/lib/mysql', 'mode': 'rw'},
        },
        'env ': [
            f"MYSQL_ROOT_PASSWORD={i6.crypto.password()}",
            'MYSQL_DATABASE=wordpress'
        ],
        'init_build': True,
        'cmd': ['sh', '-c', '/root/init.sh; bash'],
    })
    all_config_options.run()
