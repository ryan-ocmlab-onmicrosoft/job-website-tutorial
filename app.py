import os
from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__, static_url_path='/static', static_folder='static')

CONCERTS = [
    {
        'id':1,
        'Date': '2023-03-15',
        'Time': '17:30',
        'Location': '台北/中山堂'
    },
    {
        'id':2,
        'Date': '2023-03-22',
        'Time': '18:00',
        'Location': '台北/國家音樂廳'
    },
        {
        'id':3,
        'Date': '2023-03-23',
        'Time': '18:00',
        'Location': '台中/歌劇院'
    },
    {
        'id':4,
        'Date': '2023-03-29',
        'Time': '18:00',
        'Location': '高雄/衛武營'
    },
    
    {
        'id':5,
        'Date': '2023-05-31',
        'Time': '18:00',
        'Location': '基隆/文化中心'
    }

]

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def my_first_page():
    return render_template('home.html', concerts=CONCERTS)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/concerts')
def my_fourth_page():
    return render_template('concerts.html', concerts=CONCERTS)

@app.route('/google3d01949f3bff88dd.html')
def google_page():
    return render_template('google3d01949f3bff88dd.html')

@app.route('/oauth2callback', methods=['GET', 'POST'])
def oauth2callback_page():
    data=request.form
    print(data)
    return render_template('oauth2callback.html', request=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
