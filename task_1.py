import calendar

print('\nПривет Мир!\n')

print(calendar.month(2023, 3))

total_weak_price_sum = 0
total_course_sum = 0

for one_price_sum in range(100, 1100, 100):
    total_weak_price_sum += one_price_sum

print('Кол-во денег на призы за одну неделю обучения (6 месяцев) -', total_weak_price_sum)

for one_week_total_price_sum in range(6 * 4):
    total_course_sum += total_weak_price_sum

print('\nКол-во денег на призы за весь курс обучения -', total_course_sum)

students = int(input('\nВведите кол-во студентов на курсе - '))
print('\nПереплата на каждого студента за курс составит -', total_course_sum / students)

print('\nДобавил изменения после того как отложил предыдущий коммит')