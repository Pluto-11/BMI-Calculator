from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!doctype html>
<html>
<head><title>BMI Calculator</title></head>
<body>
  <h1>BMI Calculator</h1>
  <form method="post">
    Height (in cm): <input type="text" name="height"><br>
    Weight (in kg): <input type="text" name="weight"><br>
    <input type="submit" value="Calculate BMI">
  </form>
  {% if bmi %}
  <h2>Your BMI: {{ bmi }}</h2>
  {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculate_bmi():
    bmi = ''
    if request.method == 'POST':
        height_in_meters = float(request.form['height']) / 100
        weight = float(request.form['weight'])
        bmi = round(weight / (height_in_meters ** 2), 2)
    return render_template_string(HTML, bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
