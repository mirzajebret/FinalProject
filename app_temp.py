from flask import (
    Flask,
    render_template
)
import connexion
import os

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')


@app.route('/')
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", default="5000")))