'''from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form.get('name')
    gender = request.form.get('gender')
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

    if category == 'upper_body':
        return render_template('upper_body_exercises.html', user_name=user_name)
    elif category == 'lower_body':
        return render_template('lower_body_exercises.html', user_name=user_name)
    elif category == 'full_body':
        return render_template('workout.html', user_name=user_name)
    
@app.route('/workout/<user_name>')
def workout(user_name):
    return render_template('workout.html', user_name=user_name)

@app.route('/process_workout', methods=['POST'])
def process_workout():
    user_name = request.form.get('user_name')
    duration = request.form.get('duration')

    # Process the workout duration as needed

    return f"Hello {user_name}! You selected a {duration} workout duration."

@app.route('/workout_type/<user_name>')
def workout_types(user_name):
    return render_template('workout_type.html', user_name=user_name)

if __name__ == '__main__':
    app.run(debug=True)
'''
from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form.get('name')
    gender = request.form.get('gender')
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

    if category == 'upper_body':
        return render_template('upper_body_exercises.html', user_name=user_name)
    elif category == 'lower_body':
        return render_template('lower_body_exercises.html', user_name=user_name)
    elif category == 'full_body':
        return render_template('workout.html', user_name=user_name)


@app.route('/process_workout', methods=['POST'])
def process_workout():
    user_name = request.form.get('user_name')
    duration = request.form.get('duration')

    # Process the workout duration as needed
    # For demonstration, I'm just printing the values here
    print(f"User: {user_name}, Duration: {duration}")
    if duration == "30-45 mins":
        n = 5   #n is the number of workouts
    if duration == "45-60 mins":
        n = 8
    if duration == "60-75 mins":
        n = 11
    if duration == "75-90 mins":
        n = 14
    
    return f"Hello {user_name}! You selected a {duration} workout duration."


if __name__ == '__main__':
    app.run(debug=True)
