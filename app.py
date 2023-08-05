from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store student attendance data
attendance_data = {}

@app.route('/')
def index():
    return render_template('index.html', data=attendance_data)

@app.route('/submit', methods=['POST'])
def submit():
    student_name = request.form['name']
    attendance_status = request.form['attendance']

    attendance_data[student_name] = attendance_status

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)