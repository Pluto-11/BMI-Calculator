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
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 300px;
            text-align: center;
        }
        h1 {
            color: #333;
        }
        input[type="text"] {
            padding: 10px;
            margin: 10px 0;
            width: 80%;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            font-size: 1.2em;
            color: #333;
        }
        .result h2 {
            color: #4CAF50;
        }
    </style>
</head> 
<body>
    <div class="container">
        <h1>BMI Calculator</h1>
        <form method="post">
            <label for="height">Height (in cm):</label><br>
            <input type="text" name="height" id="height" required><br>
            <label for="weight">Weight (in kg):</label><br>
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
