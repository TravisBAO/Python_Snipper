

def employee_check(work_hours):

    current_max = 0
    employee_of_month = ''

    for employee, work_hour in work_hours:
        if work_hour > current_max:
            current_max = work_hour
            employee_of_month = employee
        else:
            pass
    # return (current_max, employee_of_month)
    return current_max, employee_of_month


if __name__ == '__main__':
    work_hourss = [("Abbey", 100), ("Brady", 200), ("Lesli", 300)]
    result = employee_check(work_hourss)
    print(result)
