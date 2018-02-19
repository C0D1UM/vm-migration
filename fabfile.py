import os
from datetime import datetime

from fabric.api import run, put, env, local

env.hosts = [os.environ.get('VM_HOST', '')]
env.password = os.environ.get('VM_PASSWORD', '')


def hostname_check():
    run('hostname')


def send_dir(localpath: str, remotepath: str, mode=None):
    run(f'mkdir -p {remotepath}')
    put(localpath, remotepath, mode=mode)


def send_file(localpath: str, remotepath: str, mode=None):
    put(localpath, remotepath, mode=mode)


def run_script(script: str):
    with open(script) as file:
        run(file.read())


def update_sources_list():
    put('templates/sources.list', '/etc/apt/sources.list', use_sudo=True)


def create_db(db_name: str):
    run(f'sudo -u postgres createdb {db_name}')


def drop_db(db_name: str):
    run(f'sudo -u postgres dropdb {db_name}')


def migrate_db(db_name: str, dumpfile_path='', remotepath='/root/'):
    file_name = f'{db_name}_{datetime.today().date()}' if not dumpfile_path else dumpfile_path
    send_dumped_file(db_name, file_name)
    restore_db(db_name, remotepath + file_name)


def send_dumped_file(db_name: str, dumpfile_path: str, remotepath='/root/'):
    local(f'pg_dump -h localhost -p 5432 -U postgres -F c -b -v -f "{dumpfile_path}" {db_name}')
    put(dumpfile_path, remotepath)
    local(f'rm {dumpfile_path}') 


def restore_db(db_name: str, file_name: str):
    run(f'pg_restore -c -h localhost -p 5432 -U postgres -d {db_name} -v {file_name}')


def update_postgres_password(password: str):
    run('sudo -u postgres psql -c "ALTER USER postgres PASSWORD {};";exit 0'.format(f"'{password}'"))


def set_up_minio(password: str, username='minio', url='http://localhost:9000'):
    with open('scripts/install_minio.sh') as file:
        run(file.read())

    run(f'mc config host add minio {url} {username} {password}')

    with open('scripts/update_mino_policy.sh') as file:
        run(file.read())


def setup_letsencrypt(email: str, domain: str):
    with open('scripts/install_letsencrypt.sh') as file:
        run(file.read())    
    
    run(f'letsencrypt certonly --standalone --renew-by-default --email {email} -d {domain}')
    run('sudo echo "#!/usr/bin/env bash" > /etc/cron.monthly/renew_letsencrypt.sh')
    run('sudo echo "/usr/bin/letsencrypt certonly --standalone --renew-by-default'
        f' --email {email} -d {domain}" >> /etc/cron.monthly/renew_letsencrypt.sh')
    run('sudo chmod +x /etc/cron.monthly/renew_letsencrypt.sh')
