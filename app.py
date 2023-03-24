import os
from flask import Flask, render_template, send_from_directory, request, redirect, session
from requests_oauthlib import OAuth2Session

# Credentials you get from registering a new application
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')

# OAuth endpoints given in the Google API documentation
authorization_base_url = "https://accounts.google.com/o/oauth2/v2/auth"
token_url = "https://www.googleapis.com/oauth2/v4/token"
scope = ["openid", "https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"]


app = Flask(__name__, static_url_path='/static', static_folder='static')
# app.secret_key = os.urandom(24)
app.secret_key = os.getenv('SECRET_KEY')

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
    google = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
    # Redirect user to Google for authorization
    # offline for refresh token
    # force to always make user click authorize
    authorization_url, state = google.authorization_url(authorization_base_url, access_type="offline", prompt="select_account")

    # State is used to prevent CSRF, keep this for later.
    session["oauth_session"] = google

    return redirect(authorization_url)

@app.route('/concerts')
def my_fourth_page():
    return render_template('concerts.html', concerts=CONCERTS)

@app.route('/google3d01949f3bff88dd.html')
def google_page():
    return render_template('google3d01949f3bff88dd.html')

@app.route('/oauth2callback', methods=['GET', 'POST'])
def oauth2callback_page():
    # Get the authorization verifier code from the callback url
    redirect_response = request.url

    google = session["oauth_session"]

    # Fetch the access token
    google.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)

    # Fetch a protected resource, i.e. user profile
    r = google.get('https://www.googleapis.com/oauth2/v1/userinfo')
    print('Response UserInfo :')
    print(r.content)
    return render_template('oauth2callback.html', request=form_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
