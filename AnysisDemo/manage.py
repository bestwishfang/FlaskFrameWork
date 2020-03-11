from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from AppStore import create, models


app = create()
manage = Manager(app)
migrate = Migrate(app, models)
manage.add_command('db', MigrateCommand)
app.secret_key = '123123'


if __name__ == '__main__':
    manage.run()