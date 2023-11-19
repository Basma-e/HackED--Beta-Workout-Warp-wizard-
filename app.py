from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

def workout_generator(duration, selected_exercises):
    n = 0
    if duration == "30-45":
        n = 6
    if duration == "45-60":
        n = 8
    if duration == "60-75":
        n = 10
    if duration == "75-90":
        n = 12

    exercises_mapping = {
        'Chest': [
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
            # ... other chest exercises
        ],
        'Back': [
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
            # ... other back exercises
        ],
        'Arms': [
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
            # ... other arm exercises
        ],
        'Core': ["Plank",
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
            # ... core exercises
        ],
        'Legs': ["Squats",
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
            # ... leg exercises
        ],
        'Glutes': ["Hip Thrusts",
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
            # ... glute exercises
        ]
    }

    workPerGroup = round(n / len(selected_exercises))
    workout_List = []

    for category in selected_exercises:
        if category in exercises_mapping:
            exercises_for_category = exercises_mapping[category]
            workout_List += random.sample(exercises_for_category, workPerGroup)

    return workout_List

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
    selected_exercises = request.form.getlist('exercises')  # Update this line

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
    selected_exercises = request.form.getlist('exercises')

    print(duration)
    print(selected_exercises)
    workout_List = workout_generator(duration, selected_exercises)
    print( workout_List)
    # Process the workout duration as needed
    # For demonstration, I'm just printing the values here
    print(f"User: {user_name}, Duration: {duration}")

    return redirect(url_for('display_words', words=','.join(workout_List)))

    #return redirect(url_for('display_words', words=workout_List))

@app.route('/display_words')
def display_words():
    # Pass the word_list to the template
    workout_List = request.args.get('words', '').split(',')

    #workout_List = request.args.get('words', '').split(',')
    print(workout_List)
    return render_template('workout_display.html', words=workout_List)

if __name__ == '__main__':
    app.run(debug=True)
