from app import app

app_name = 'Stepper'


@app.route('/')
@app.route('/index')
def index():
    return 'Welcome to %s!' % (app_name)
