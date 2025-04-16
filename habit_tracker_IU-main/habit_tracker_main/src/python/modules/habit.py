from datetime import date

class Habit:
    def __init__(self, name, category, frequency):
        self.name = name
        self.category = category
        self.frequency = frequency
        self.check_ins = []

    def check_in(self, checkin_date=None):
        if checkin_date is None:
            checkin_date = date.today()
        if checkin_date not in self.check_ins:
            self.check_ins.append(checkin_date)

    def get_streak(self):
        return len(self.check_ins)

    def __str__(self):
        return f"{self.name} ({self.frequency}) - {len(self.check_ins)} check-ins"
