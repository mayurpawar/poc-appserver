from flask import Flask, render_template, Response
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./apis/specs/')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')
application = app.app

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return Response(status=200, mimetype='application/json')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)