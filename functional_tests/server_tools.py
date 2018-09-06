from fabric.api import run, env, cd, hosts
from fabric.context_managers import settings, shell_env


env.host_string = 'ec2-13-209-42-75.ap-northeast-2.compute.amazonaws.com'
env.user = 'ubuntu'
env.key_filename = ['~/dev/key/awdpwd.pem']
sites = 'superlists-test.com'


def _get_manage_dot_py(host):
    run(f'pyenv activate {sites}')
    return f'~/.pyenv/versions/3.6.5/envs/{sites}/bin/python ~/sites/{sites}/manage.py'


def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'ubuntu@ec2-13-209-42-75.ap-northeast-2.compute.amazonaws.com'), cd(f'~/sites/{sites}'):
        run(f'{manage_dot_py} flush --noinput')


def _get_server_env_vars(host):
    env_lines = run(f'cat ~/sites/{sites}/.env').splitlines()
    return dict(l.split('=') for l in env_lines if l)


def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py(sites)
    with settings(host_string=f'ubuntu@ec2-13-209-42-75.ap-northeast-2.compute.amazonaws.com'), cd(f'~/sites/{sites}'):
        session_key = run(f'{manage_dot_py} create_session {email}')
        return session_key.strip()
