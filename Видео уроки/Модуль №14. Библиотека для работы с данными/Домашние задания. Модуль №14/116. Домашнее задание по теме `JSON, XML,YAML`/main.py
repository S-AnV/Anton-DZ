import json

def employees_rewrite(sort_type):
    with open('employees.json', 'r') as json_file:
        loaded_json = json.load(json_file)
        number_of_users = loaded_json['employees']
        try:
            if sort_type == 'salary':
                sorted_key = {'employees': sorted(number_of_users, key=lambda x: x[sort_type], reverse=True)}
            elif sort_type == 'firstName' or 'lastName' or 'department':
                sorted_key = {'employees': sorted(number_of_users, key=lambda x: x[sort_type])}
        except Exception:
            raise ValueError('Bad key for sorting')


    # print(sorted_firstName)

    if sort_type == 'firstName':
        with open('employees_firstName_sorted.json', 'w') as json_file:
            json.dump(sorted_key, json_file, indent=4)
    elif sort_type == 'lastName':
        with open('employees_lastName_sorted.json', 'w') as json_file:
            json.dump(sorted_key, json_file, indent=4)
    elif sort_type == 'department':
        with open('employees_department_sorted.json', 'w') as json_file:
            json.dump(sorted_key, json_file, indent=4)
    else:
        with open('employees_salary_sorted.json', 'w') as json_file:
            json.dump(sorted_key, json_file, indent=4)

employees_rewrite('salary')