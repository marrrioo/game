class Car:
    def __init__(self, number,model,color):              
        self.number = number                            
        self.model = model
        self.color = color                   

    def showInfo(self):                                                          #вывод машины
        return{'Номер':self.number, 'Модель':self.model, 'Цвет':self.color}

    def setmodel(self,newmodel):                                                 #изменять маишну
        self.model = newmodel      

arr = []

while True:
    
    print('Создать автомобиль')
    number = input('номер')
    model = input('модель')
    color = input('цвет')
    car = Car(number, model, color)
    arr.append(car)
    # print('Номер:', car.number, 'Модель:', car.model, 'Цвет:', car.color)
    answer = input('continue(yes/no)????')
    if answer == 'no':
        break
    
    
    if answer == 2:
        print('Показать машины')
        for i in arr:
            print('Номер:'+ i.number+'Модель:'+ i.model+'Цвет:'+ i.color)



 #изменять маишну