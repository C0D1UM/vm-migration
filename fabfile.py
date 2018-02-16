from fabric.api import run, put


def hostname_check():
    run('hostname')


def send_dir(localpath: str, remotepath: str, mode=None):
    run(f'mkdir -p {remotepath}')
    put(localpath, remotepath, mode)


def run_script(script: str):
    with open(script) as file:
        run(file.read())


def update_sources_list():
    put('templates/sources.list', '/etc/apt/sources.list', use_sudo=True)


def create_db(db_name: str):
    # could not change directory to "/root": Permission denied
    # it's ok if the above message is returned after the command is done
    run(f'sudo -u postgres createdb {db_name}')
