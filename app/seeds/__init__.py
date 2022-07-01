from flask.cli import AppGroup

from .users import seed_users, under_users

seed_commands = AppGroup('seed')


@seed_commands.command('all')
def seed():
    seed_users()


@seed_commands.command('undo')
def undo():
    under_users()
