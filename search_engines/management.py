import click

from search_engines.es import es


@click.group()
def cmd():
    pass


@cmd.command('insert')
def insert():
    es.ES().insert()


if __name__ == '__main__':
    cmd()
