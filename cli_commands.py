import click
from flask.cli import with_appcontext
from create_admin import create_admin_user

@click.command('create-admin')
@with_appcontext
def create_admin():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    create_admin_user(username, password)
