from datetime import datetime


class SuperDate(datetime):
    def __init__(self, year, month, day, hour):
        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
    def get_season(self):
        """
        возвращает сезон года (Summer, Autumn, Winter, Spring)
        :return:
        """
        if 1 <= self._month <= 12:
            if 3 <= self._month <= 5:
                return 'Spring'
            elif 6 <= self._month <= 8:
                return 'Summer'
            elif 9 <= self._month <= 11:
                return 'Autumn'
            else:
                return 'Winter'
        else:
            return 'Введен некорректный номер месяца'

    def get_time_of_day(self):
        """
        возвращает время суток (Morning: 6-12; Day: 12-18, Evening: 18-0, Night: 0-6)
        :return:
        """
        if 6 <= self._hour <= 11:
            return 'Morning'
        elif 12 <= self._hour <= 17:
            return 'Day'
        elif 18 <= self._hour <= 23:
            return 'Evening'
        elif 0 <= self._hour <= 5:
            return 'Night'
        else:
            return 'Введено некорректное значение часа'


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())




