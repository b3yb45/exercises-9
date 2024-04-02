class TrafficLight:
    __permissible_values = ["Зеленый", "Желтый", "Красный"]
    def __init__(self):
        self.__flag = False
        self.__current_signal = 0

    def current_signal(self):
        return self.__permissible_values[self.__current_signal]

    def next_signal(self):
        if self.__current_signal == 2:
            self.__flag = True
        elif self.__current_signal == 0:
            self.__flag = False
        
        if self.__flag:
            self.__current_signal -= 1
        else:
            self.__current_signal += 1


svtfr = TrafficLight()
for _ in range(10):
    print(svtfr.current_signal())
    svtfr.next_signal()
