# The specification of this program is below :
# 1. Create a Flask app
# 2. Create a route for the home page
# 3. Create a route for the about page
# 4. Create a route for the contact page
# 5. Create a route for the concerts page
# 6. Create a route for the tickets page
# 7. Create a route for the login page
# 8. Create a route for the register page
# 9. Create a route for the logout page
# 10. Create a route for the admin page
# 11. Create a route for the admin concerts page
# 12. Create a route for the admin concerts add page
# 13. Create a route for the admin concerts edit page
# 14. Create a route for the admin concerts delete page
# 15. Create a route for the admin tickets page
# 16. Create a route for the admin tickets add page
# 17. Create a route for the admin tickets edit page
# 18. Create a route for the admin tickets delete page
# 19. Create a route for the admin users page
# 20. Create a route for the admin users add page
# 21. Create a route for the admin users edit page
# 22. Create a route for the admin users delete page
# 23. Create a route for the admin users login page
# 24. Create a route for the admin users register page
# 25. Create a route for the admin users logout page
# 26. Create a route for the admin users profile page
# 27. Create a route for the admin users profile edit page
# 28. Create a route for the admin users profile delete page
# 29. Create a route for the admin users profile password page
# 30. Create a route for the admin users profile password edit page
# 31. Create a route for the admin users profile password delete page
# 32. Create a route for the admin users profile password change page
# 33. Create a route for the admin users profile password change edit page
# 34. Create a route for the admin users profile password change delete page
# 35. Create a route for the admin users profile password change confirm page
# 36. Create a route for the admin users profile password change confirm edit page
# 37. Create a route for the admin users profile password change confirm delete page
# 38. Create a route for the admin users profile password change confirm cancel page
# 39. Create a route for the admin users profile password change confirm cancel edit page
# 40. Create a route for the admin users profile password change confirm cancel delete page

import os
from flask import Flask, render_template, send_from_directory

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

@app.route('/oauth2callback')
def oauth2callback_page():
    return render_template('oauth2callback.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
