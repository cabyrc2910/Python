def view_data(data, title):   
    print(f'sum = {data}')        #  value = 1    Value = 2     sum = 3    для суммы
    print(f'result = {data}')      #  value = 2    Value = 5     sum = 10     для произведения 
    print(f'{title} = {data}')     #

def get_value():
    return int(input('value = '))  