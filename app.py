from flask import Flask, request, jsonify,render_template
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('email_validation.html')

@app.route('/validate_email', methods=['GET','POST'])
def validate_email():
    email = request.form.get('email')
    # Regular expression for validating an email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Using re.match() function to check if the email address matches the pattern
    if re.match(pattern, email):
        result='{} is a valid Email'.format(email)
        return render_template('result.html',result=result)
    else:
        result='{} is not a valid Email'.format(email)
        return render_template('result.html',result=result)


if __name__ == '__main__':
    app.run(debug=True)
