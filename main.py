from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = ''' 
<!doctype html> 
<html> 
<head>
    <title>BMI Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
            text-align: center;
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 0.8s ease-out forwards;
        }
        h1 {
            color: #333;
            font-size: 1.8em;
            margin-bottom: 20px;
        }
        label {
            margin-top: 10px;
            color: #555;
            font-size: 1.1em;
            display: block;
            text-align: left;
            width: 100%;
        }
        input[type="text"] {
            padding: 10px;
            margin: 10px 0;
            width: 100%;
            border-radius: 5px;
            border: 1px solid #ddd;
            font-size: 1.1em;
            box-sizing: border-box; /* Ensures padding and borders don't affect width */
            transition: all 0.3s ease;
        }
        input[type="text"]:focus {
            border-color: #4CAF50;
            box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 12px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
            font-size: 1.2em;
            transition: background-color 0.3s ease;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            font-size: 1.2em;
            color: #333;
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 0.8s ease-out forwards 0.5s;
        }
        .result h2 {
            color: #4CAF50;
        }
        /* Responsive Design */
        @media (max-width: 600px) {
            h1 {
                font-size: 1.5em;
            }
            .container {
                padding: 15px;
                width: 95%;
                max-width: 350px;
            }
            label {
                font-size: 1em;
            }
            input[type="text"], input[type="submit"] {
                font-size: 1em;
            }
        }

        /* Animation Keyframes */
        @keyframes fadeInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head> 
<body>
    <div class="container">
        <h1>BMI Calculator</h1>
        <form method="post">
            <label for="height">Height (in cm):</label>
            <input type="text" name="height" id="height" required><br>
            <label for="weight">Weight (in kg):</label>
            <input type="text" name="weight" id="weight" required><br>
            <input type="submit" value="Calculate BMI">
        </form>
        {% if bmi %}
        <div class="result">
            <h2>Your BMI: {{ bmi }}</h2>
        </div>
        {% endif %}
    </div>
</body> 
</html> 
'''

@app.route('/', methods=['GET', 'POST'])
def calculate_bmi():
    bmi = ''
    if request.method == 'POST':
        try:
            height_in_meters = float(request.form['height']) / 100  # Convert height from cm to meters
            weight = float(request.form['weight'])
            bmi = round(weight / (height_in_meters ** 2), 2)  # Calculate BMI
        except ValueError:
            bmi = 'Invalid input. Please enter valid numbers.'
    return render_template_string(HTML, bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
