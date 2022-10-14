# import model_sum as model   #  складывать
# import model_sub as model   #  отнимать
import  model_mult as model    #  умножать
import view

def button_click():
    value_a = view.get_value()   # данные 1 числа
    value_b = view.get_value()    #  данные 2 числа
    model.init(value_a, value_b)    #  инициализируем входные данные нашей модели передав аргументы (value)
    result = model.do_it()           
    # result = model.sum()           # вычисляем сумму  
    # result = model.mult()          # вычисляем произведение
    view.view_data(result, "result")     #  "mult" или  "sum"  "sub"