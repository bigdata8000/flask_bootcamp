from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')     # 127.0.0.1:5000
def index():
    z = 'Mr Python 2021'
    y = 'Rabbit, Bird, Fish, Elephant, Turtle, Horse.'
    car_dict = {'make':'Tesla', 'model':'roadster'}
    return render_template('basic.html', z=z, y=y, car_dict=car_dict)


@app.route('/about')
def about():
    mylist = ['Nissan', 'Tesla', 'Honda', 'Porche', 'Audi', 'BMW', 'Ford']
    return render_template('about.html', mylist=mylist)


if __name__ == '__main__':
    app.run(debug=True)

