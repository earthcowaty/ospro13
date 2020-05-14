from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('Home.html')


@app.route('/testcb', methods=['GET', 'POST'])
def tez():
    if request.method == 'POST':
        num1 = request.form.get('num1',None)
        num2 = request.form.get('num2',None)
        num3 = request.form.get('num3',None)
        num4 = request.form.get('num4',None)
        num5 = request.form.get('num5',None)
        num6 = request.form.get('num6',None)
        print(num1)
        if not num1 or not num2 or not num3 or not num4 or not num5 or not num6:
            alert = "Fill in not complete please try again"
            return render_template('Test.html',alert=alert)
        sum = int(num1) + int(num2) + int(num3) + int(num4) + int(num5) + int(num6)

        if sum == 231:
            return render_template('Result1.html')
        else:
            return render_template('Result2.html')
    elif request.method == 'GET':
        return render_template('Test.html')




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
