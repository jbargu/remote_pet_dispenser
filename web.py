from flask import (
    Flask,
    render_template,
)
from servo_controller import ServoController

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dispense')
def dispense():
    ServoController().dispense()
    return 'Yiiiisss I very good doggo!'
    

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8082)

