# coding: utf-8
from app import create_app
from app.Extensions import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from config.runConfig import ProductionConfig

app = create_app(ProductionConfig)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)
manager.add_command("runserver", Server(port=ProductionConfig.RUNSERVER_PORT, host=ProductionConfig.RUNSERVER_IP, use_debugger=ProductionConfig.DEBUG))

if __name__ == '__main__':
    manager.run()