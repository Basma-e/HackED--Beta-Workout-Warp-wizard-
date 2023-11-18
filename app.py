from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form.get('name')
    gender = request.form.get('gender')

    # Redirect to the workout page with user name as a query parameter
    return redirect(url_for('workout', user_name=user_name))

@app.route('/workout')
def workout():
    # Render the workout.html template
    return render_template('workout.html')

@app.route('/process_workout', methods=['POST'])
def process_workout():
    user_name = request.form.get('user_name')
    duration = request.form.get('duration')

    # Process the workout duration as needed

    return f"Hello {user_name}! You selected a {duration} workout duration."

if __name__ == '__main__':
    app.run(debug=True)
