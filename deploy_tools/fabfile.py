import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run


REPO_URL = 'https://github.com/olvt01/TDD_Django.git'
env.user = "ubuntu"
env.key_filename = ['~/dev/key/awdpwd.pem']
env.hosts = ['ec2-13-209-42-75.ap-northeast-2.compute.amazonaws.com']


def local_uname():
    local('uname -a')

def remote_uname():
    run('uname -a')


def deploy():
    site_folder = f'/home/ubuntu/sites/{env.sites}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_pyenv_virtualenv()  # must
        #_create_or_update_dotenv()
        _update_static_files()
        _update_database()
        # run('echo "d" > "a"')


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')


def _install_pyenv():
    pass


def _update_pyenv_virtualenv():
    if not exists(f'~/.pyenv/versions/{env.sites}'):
        run(f'pyenv virtualenv 3.6.5 {env.sites}')
    run(f'pyenv activate {env.sites}')
    run(f'~/.pyenv/versions/{env.sites}/bin/pip install -r requirements.txt')


def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITENAME={env.host}')
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')


def _update_static_files():
    run(f'~/.pyenv/versions/{env.sites}/bin/python manage.py collectstatic --noinput')


def _update_database():
    run(f'~/.pyenv/versions/{env.sites}/bin/python manage.py migrate --noinput')



