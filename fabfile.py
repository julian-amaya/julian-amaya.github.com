from fabric.context_managers import prefix
from fabric.api import local


def go_code(func):
    def decorator(*args, **kwargs):
        with prefix('cd le_code'):
            # with prefix('source /usr/local/bin/virtualenvwrapper.sh'):
            return func(*args, **kwargs)
    return decorator


@go_code
def generate():
    local('pelican . -o ../ -s publishconf.py')
