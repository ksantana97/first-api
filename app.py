from flask import (
    Flask, 
    render_template, 
    request, 
    url_for
)

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':

        weight, reps = float(request.form['Weight (Kg)']), float(request.form['Repetitions'])
        RM = round(weight/(1.0278 - 0.0278 * reps),2)
        return render_template('index.html', rm=RM)

    else:
        
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)