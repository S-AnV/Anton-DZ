from datetime import datetime


class SuperDate(datetime):

    def get_season(self):
        """
        возвращает сезон года (Summer, Autumn, Winter, Spring)
        :return:
        """
        if 3 <= self.month <= 5:
            return 'Spring'
        elif 6 <= self.month <= 8:
            return 'Summer'
        elif 9 <= self.month <= 11:
            return 'Autumn'
        else:
            return 'Winter'


    def get_time_of_day(self):
        """
        возвращает время суток (Morning: 6-12; Day: 12-18, Evening: 18-0, Night: 0-6)
        :return:
        """
        if 6 <= self.hour <= 11:
            return 'Morning'
        elif 12 <= self.hour <= 17:
            return 'Day'
        elif 18 <= self.hour <= 23:
            return 'Evening'
        elif 0 <= self.hour <= 5:
            return 'Night'



a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())




