import csv

def write_holiday_cities(first_letter):
    have_visited = set()
    want_to_visit = set()
    have_visited_str = 'Посетили:'
    want_to_visit_str = 'Хотят посетить:'
    no_one_has_been_to_str = 'Никогда не были в:'
    we_will_go_to_str = 'Следующим городом будет:'

    with open('travel-notes.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:

            """Находим города, которые уже посетили"""
            a = str.split(row[1], sep=';')
            while row[0][0] == first_letter:
                for x in a:
                    have_visited.add(x)
                break
            have_visited_list = sorted(have_visited)

            """Находим города, которые хотят посетить"""
            b = str.split(row[2], sep=';')
            while row[0][0] == first_letter:
                for x in b:
                    want_to_visit.add(x)
                break
            want_to_visit_list = sorted(want_to_visit)

            """Города, в которых не были"""
            sd = want_to_visit_list + have_visited_list
            no_one_has_been_to = []
            for i in sd:
                while i not in have_visited_list:
                    no_one_has_been_to.append(i)
                    break

        """Определяем следующий для посещения город"""
        we_will_go_to_list = [want_to_visit_list[0]]

        # print(have_visited_list)
        # print(want_to_visit_list)
        # print(no_one_has_been_to)
        # print(we_will_go_to_list)

    with open('holiday.csv', 'a', newline='', encoding='utf-8') as out_csv:
        writer = csv.writer(out_csv)

        writer.writerow(have_visited_str.split())
        writer.writerow(have_visited_list)

        writer.writerow(want_to_visit_str.split(sep=','))
        writer.writerow(want_to_visit_list)

        writer.writerow(no_one_has_been_to_str.split(sep=','))
        writer.writerow(no_one_has_been_to)

        writer.writerow(we_will_go_to_str.split(sep=','))
        writer.writerow(we_will_go_to_list)


write_holiday_cities('L')
write_holiday_cities('R')


