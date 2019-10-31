class Clock: 
    def __init__(self):
        self.__seconds = Counter("Seconds")
        self.__minutes = Counter("Minutes")
        self.__hours = Counter("Hours")

    def Tick(self):
        self.__seconds.Increment()
        if (self.__seconds.Value == 60):
            self.__seconds.Reset()
            self.__minutes.Increment()
        if (self.__minutes.Value == 60):
            self.__minutes.Reset()
            self.__hours.Increment()
        if (self.__hours.Value == 24):
            self.Reset()

    def Reset(self):
        self.__seconds.Reset()
        self.__minutes.Reset()
        self.__hours.Reset()

    @property
    def Time(self):
        return f"{self.__hours.Value:02}:{self.__minutes.Value:02}:{self.__seconds.Value:02}"

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name=value

class Counter: 
    def __init__(self, name):
        self.__name=name
        self.__count=0

    def Increment(self):
        self.__count += 1

    def Reset(self):
        self.__count = 0

    @property
    def Value(self):
        return self.__count

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name=value

c1 = Clock()
for i in range(86401):
  print(c1.Time)
  c1.Tick()
