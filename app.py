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

@app.route('/workout/<user_name>')
def workout(user_name):
    return render_template('workout.html', user_name=user_name)

@app.route('/process_workout', methods=['POST'])
def process_workout():
    user_name = request.form.get('user_name')
    duration = request.form.get('duration')

    # Process the workout duration as needed

    # Redirect to the next section based on the chosen duration
    return redirect(url_for('extended_workout', user_name=user_name))

@app.route('/extended_workout/<user_name>')
def extended_workout(user_name):
    return render_template('workout_type.html', user_name=user_name)

@app.route('/choose_exercises', methods=['POST'])
def choose_exercises():
    user_name = request.form.get('user_name')
    category = request.form.get('category')
    selected_exercises = request.form.getlist('exercises')

    # Process the selected exercises as needed
    # For demonstration, I'm just printing the values here
    print(f"User: {user_name}, Category: {category}, Exercises: {', '.join(selected_exercises)}")

    # You can save these values to local variables or a database if needed

    return f"Hello {user_name}! You selected {', '.join(selected_exercises)} for {category} workout."

if __name__ == '__main__':
    app.run(debug=True)
