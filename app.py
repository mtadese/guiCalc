#importing the Flask module and creating a Flask web server
from flask import Flask, render_template, request

#import maths function
import math 

try:

    #the current file representing my web application
    app = Flask(__name__)

    #the app's default page
    @app.route('/')
    def main():
        return render_template('app.html')


    @app.route('/send', methods=['POST'])

    def send(sum=sum):
        if request.method == 'POST':
            num1 = request.form['num1']
            num2 = request.form['num2']
            operation = request.form['operation']

            if operation == 'add':
                sum = float(num1) + float(num2)
                return render_template('app.html', sum=sum)

            elif operation == 'subtract':
                sum = float(num1) - float(num2)
                return render_template('app.html', sum=sum)

            elif operation == 'multiply':
                sum = float(num1) * float(num2)
                return render_template('app.html', sum=sum)

            elif operation == 'divide':
                sum = float(num1) / float(num2)
                return render_template('app.html', sum=sum)

            elif operation == 'squared':
                sum = (float(num1))**2
                return render_template('app.html', sum=sum)
            
            elif operation == 'squarert':
                #sum = math.sqrt(float(num1))
                sum = (float(num1)) ** 0.5 
                return render_template('app.html', sum=sum)
            

            else:
                return render_template('app.html')


    if __name__ == "__main__":
        app.run(debug=True)

except Exception as e:
    print('Error Message: ',e)
    