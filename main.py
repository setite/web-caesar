from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form method="POST">
        <label for="rot">Rotate by:</label>
            <input      type="number" name="rot" value="0"/>
            <textarea   type="text" name="text">{0}</textarea>
            <br>
            <input type="submit" value="Squanch It!"/>
        </form>
        
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    # rot = []
    # text = ""
    rot = int(request.form['rot'])
    text = str(request.form['text'])

    rotation = rotate_string(text, rot)
    # sentence = "<h1>" + rotate_string(text, rot) + "</h1>"

    return form.format(rotation)


@app.route("/")
def index():
    # content = form
    
    return form.format('')


app.run()