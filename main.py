#Импорт
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    TRANSPORT = {
        1: 0,     
        2: 500,   
        3: 2000   
    }
    
    FOOD = {
        3: 50,    
        7: 300,  
        10: 600,  
        12: 1000  
    }
    
    DEVICES = {
        4: 200,   
        7: 500,  
        10: 1000  
    }
    
    total_co2 = TRANSPORT.get(int(size), 0) + FOOD.get(int(lights), 0) + DEVICES.get(int(device), 0)
    return total_co2

#Первая страница
@app.route('/')  
def index():
    return render_template('globalwarming.html')

#
@app.route('/calculator')
def calculator():
    return render_template('index.html')

#Вторая страница
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

#Третья страница
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

#Расчет
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
#Форма
@app.route('/form')
def form():
    return render_template('form.html')

#Результаты формы
@app.route('/submit', methods=['POST'])
def submit_form():
    #Создай переменные для сбора информации
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

    # здесь вы можете сохранить данные или отправить их по электронной почте
    return render_template('form_result.html', 
                           #Помести переменные
                           name=name,
                           email=email,
                           address=address,
                           date=date
                           )

@app.route('/globalwarming')
def globalwarming():
    return render_template('globalwarming.html')

app.run(debug=True)