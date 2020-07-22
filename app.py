from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

#the folder where the uploaded photos will be stored
app.config['UPLOADED_PHOTOS_DEST'] = 'images'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:6284085887@127.0.0.1/engage'
app.config['DEBUG'] = True #because we have used manage.run instead of app.run(debug=True)
app.config['SECRET_KEY'] = 'sdfjbuogfelrfgualfuaweflwriofalsdfoudf'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

configure_uploads(app, photos)

db = SQLAlchemy(app)
migrate = Migrate(app, db)



@app.template_filter('time_since')
def time_since(delta):

	seconds = delta.total_seconds()

	days,seconds = divmod(seconds, 86400)
	hours,seconds = divmod(seconds, 3600)
	minutes,seconds = divmod(seconds, 60)

	if days > 0:
		return "%dd" %(days)
	elif hours > 0:
		return "%dh" %(hours)
	elif minutes > 0:
		return "%dm" %(minutes)
	else:
		return 'Just Now'

from views import *

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()


# initiate flask migrate
# python app.py db init
# python app.py db migrate
# python app.py db upgrade
# python app.py 
# python app.py runserver
