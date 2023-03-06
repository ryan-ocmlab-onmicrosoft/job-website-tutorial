from flask import Flask, render_template

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

@app.route('/')
def my_first_page():
    return render_template('home.html', concerts=CONCERTS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
