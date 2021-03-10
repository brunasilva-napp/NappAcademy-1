from datetime import datetime, date

class MyCalendar:
    def __init__(self, *args) -> None:
        self.datas = []
        self.add_holiday(*args)

    def add_holiday(self, *args) -> None:
        for data in args:
            x = self.teste(data)
            if x:
                self.datas.append(x)
        self.datas = list(set(self.datas))

    def teste(self, data) -> date:

        if isinstance(data, date):
            return data
            
        elif isinstance(data, str):
            try:
                tdate = datetime.strptime(data, '%d/%m/%Y').date()
                return tdate
            except:
                return None
    
    def check_holiday(self, data) -> bool:
        check = self.teste(data) in self.datas
        return check