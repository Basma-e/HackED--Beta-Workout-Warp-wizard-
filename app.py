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
app.secret_key = 'your_secret_key'  # Set a secret key for the session, replace with a secure key in production

def workout_generator(duration):

    if duration == "30-45 mins":
        n = 6    #n is the number of workouts
    if duration == "45-60 mins":
        n = 8
    if duration == "60-75 mins":
        n = 10
    if duration == "75-90 mins":
        n = 12

    chest = [
        "Barbell Bench Press",
        "Dumbbell Bench Press",
        "Incline Bench Press",
        "Decline Bench Press",
        "Push-Ups",
        "Chest Dips",
        "Chest Flyes",
        "Cable Crossover",
        "Pec Deck Machine",
        "Medicine Ball Push-Ups",
        "Landmine Press",
        "Machine Chest Press",
        "Plyometric Push-Ups",
        "Single-Arm Dumbbell Press"
    ]
    back = [
        "Pull-Ups",
        "Deadlifts",
        "Bent-Over Rows",
        "Lat Pulldowns",
        "T-Bar Rows",
        "Seated Cable Rows",
        "Chin-Ups",
        "One-Arm Dumbbell Rows",
        "Hyperextensions",
        "Good Mornings",
        "Reverse Flyes",
        "Pullovers",
        "Shrugs",
        "Rack Pulls"
    ]
    arm = [
        "Bicep Curls",
        "Tricep Dips",
        "Hammer Curls",
        "Tricep Extensions",
        "Preacher Curls",
        "Skull Crushers",
        "Concentration Curls",
        "Tricep Kickbacks",
        "Reverse Curls",
        "Overhead Tricep Press",
        "Zottman Curls",
        "Close-Grip Bench Press",
        "Barbell Curls",
        "Rope Pushdowns"
    ]
    core = [
        "Plank",
        "Russian Twists",
        "Crunches",
        "Leg Raises",
        "Mountain Climbers",
        "Bicycle Crunches",
        "Hanging Leg Raises",
        "Woodchoppers",
        "Dead Bug Exercise",
        "Ab Rollouts",
        "Side Plank",
        "Flutter Kicks",
        "Hollow Body Hold",
        "Medicine Ball Slams"
    ]

    leg = [
        "Squats",
        "Lunges",
        "Deadlifts",
        "Leg Press",
        "Leg Curls",
        "Calf Raises",
        "Step-Ups",
        "Romanian Deadlifts",
        "Box Jumps",
        "Glute Bridges",
        "Hack Squats",
        "Bulgarian Split Squats",
        "Walking Lunges",
        "Seated Calf Raises"
    ]

    glute = [
        "Hip Thrusts",
        "Lunges",
        "Deadlifts",
        "Glute Bridges",
        "Donkey Kicks",
        "Fire Hydrants",
        "Sumo Squats",
        "Bulgarian Split Squats",
        "Clamshells",
        "Step-Ups",
        "Cable Kickbacks",
        "Single-Leg Glute Bridges",
        "Barbell Hip Thrusts",
        "Resistance Band Walks"
    ]
    workPerGroup = round(n/len(muscle_group))
    workout_List = []
    for word in muscle_group:
        workout_List += random.sample(word,workPerGroup)
    return workout_List

def muscle_group(selected_exercises):
    select_group_list = list(selected_exercises)
    return select_group_list

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

    muscle_group(selected_exercises)
    # Process the selected exercises as needed
    # For demonstration, I'm just printing the values here
    print(f"User: {user_name}, Category: {category}, Exercises: {', '.join(selected_exercises)}")

    # You can save these values to local variables or a database if needed

    if category == 'upper_body':
        return render_template('upper_body_exercises.html', user_name=user_name)
    elif category == 'lower_body':
        return render_template('lower_body_exercises.html', user_name=user_name)
    elif category == 'full_body':
        return render_template('full_body.html', user_name=user_name)


@app.route('/process_workout', methods=['POST'])
def process_workout():
    user_name = request.form.get('user_name')
    duration = request.form.get('duration')
    workout_List = workout_generator(duration)
    
    # Process the workout duration as needed
    # For demonstration, I'm just printing the values here
    print(f"User: {user_name}, Duration: {duration}")
    
    return redirect(url_for('display_words', words=workout_List))

@app.route('/display_words')
def display_words():
    # Pass the word_list to the template
    workout_List = request.args.get('words', '').split(',')

    return render_template('workout_display.html', words=workout_List)

if __name__ == '__main__':
    app.run(debug=True)
