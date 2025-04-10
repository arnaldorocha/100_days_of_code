def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 'Leap'
            else:
                return 'Not Leap'
        else:
            return 'Leap'
    else:
        return 'Not Leap'


print(is_leap_year(2024))
print(is_leap_year(2025))
print(is_leap_year(2026))
print(is_leap_year(2027))
print(is_leap_year(2028))

