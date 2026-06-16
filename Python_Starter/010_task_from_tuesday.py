'''
🔹 1. Простий відсоток (база)
Написати функцію simple_interest(sum, rate, years), яка обчислює прості відсотки.
Завдання:
Користувач вводить суму, ставку (%) і роки
Вивести прибуток і кінцеву суму
# '''
#
# def simple_interest(sum, rate, years):
#     return sum * rate / 100 * years, sum + sum * rate / 100 * years
#
#
# sum = float(input("Write your sum: "))
# rate = float(input("Write your rate in percent: "))
# years = int(input("Write your number of years: "))
#
# print("Profit:", simple_interest(sum, rate, years)[0])
# print("Full amount:", simple_interest(sum, rate, years)[1])


'''
🔹 2. Складні відсотки
Функція compound_interest(sum, rate, years)
Завдання:
Обчислити суму депозиту зі складними відсотками
Відсотки нараховуються щороку
'''

#
# def compound_interest(sum, rate, years):
#     first_sum = sum
#     for i in range(years):
#         sum = sum + sum * rate / 100
#     profit = sum - first_sum
#
#     return sum, profit
#
# sum = float(input("Write your sum: "))
# rate = float(input("Write your rate in percent: "))
# years = int(input("Write your number of years: "))
#
# print("Profit:", compound_interest(sum, rate, years)[0])
# print("Full amount:", compound_interest(sum, rate, years)[1])



'''
🔹 3. Щомісячні нарахування
Функція monthly_compound(sum, rate, months)
Завдання:
Відсотки нараховуються щомісяця
Вивести кінцеву суму
'''

# def monthly_compound(sum, rate, months):
#     for month in range(1, months + 1):
#         sum = sum + sum * rate / 100
#         print(f"Month {month}: {sum}")
#     return sum
#
#
# user_sum = float(input("Enter your amount: "))
# user_rate = float(input("Enter your rate: "))
# user_months = int(input("Enter your number of months: "))
#
# final_amount = monthly_compound(user_sum, user_rate, user_months)
#
# print(f"Amount in {user_months} month is {final_amount} dollars")



'''
🔹 4. Функція вибору типу депозиту
Створити функцію calculate_deposit(type, sum, rate, time)
Завдання:
type: "simple" або "compound"
Викликати відповідну функцію
Повернути результат
'''


# def simple_type_deposit(sum, rate, time):
#     sum = sum + sum * rate / 100 * time
#     # print("Your sum is: ", sum)
#     return sum
#
#
# def compound_type_deposit(sum, rate, time):
#     first_sum = sum
#     for i in range(time):
#         sum = sum + sum * rate / 100
#         profit = sum - first_sum
#         # print("Your profit is: ", profit)
#     return sum, profit
#
#
# def calculate_deposit(type, sum, rate, time):
#     if type == "simple":
#         final_amount = simple_type_deposit(sum, rate, time)
#         print("Your sum is: ", final_amount)
#     elif type == "compound":
#         final_amount = compound_type_deposit(sum, rate, time)
#         print("Your profit is: ", final_amount)
#     else:
#         return "enter valid type"
# # есть две разные функции для них надо сaоздать отдельные аттрибуты а также изменить последжнюю функцию  есть сложные и легкие проценты
# # можно сделать третью только для вывода в shell
#
# user_type = input("Please choose your type --> simple or compound")
# user_sum = float(input("Enter your sum: "))
# user_rate = float(input("Enter your rate in percent: "))
# user_time = int(input("Enter your number of years: "))
#
# full_amount = calculate_deposit(user_type, user_sum, user_rate, user_time)



'''
🔹 5. Розрахунок щомісячного платежу (кредит)
Функція monthly_payment(loan, rate, months)
Завдання:
Обчислити щомісячний платіж (аннуїтет)
Використати формулу ануїтету
'''

# def monthly_payment(loan, rate, months):
#     i = rate / (100 * 12)
#     monthly_payment = loan * (i * (1 + i) ** months) / ((1 + i) ** months - 1)
#     return monthly_payment
#
#
# user_loan = float(input("Enter your loan: "))
# user_rate = float(input("Enter your rate: "))
# user_months = int(input("Enter your months: "))
#
# loan_payment = monthly_payment(user_loan, user_rate, user_months)
# print("Your monthly payment is: ", loan_payment)


'''
🔹 6. Переплата по кредиту
Функція loan_overpayment(loan, rate, months)
Завдання:
Використати попередню функцію
Обчислити загальну переплату
'''

# def loan_overpayment(loan, rate, months):
#     return loan * (rate / 100) * months
#
#
#
# user_loan = float(input("Enter your loan: "))
# user_rate = float(input("Enter your rate: "))
# user_months = int(input("Enter your months: "))
#
# user_overpayment = loan_overpayment(user_loan, user_rate, user_months)
#
# print("Your overpayment is: ", user_overpayment)




'''
🔹 7. Графік платежів
Функція payment_schedule(loan, rate, months)
Завдання:
Вивести таблицю:
місяць
платіж
залишок боргу
'''
# def monthly_payment(loan, rate, months):
#     i = rate / (100 * 12)
#     user_monthly_payment = loan * (i * (1 + i) ** months) / ((1 + i) ** months - 1)
#     return user_monthly_payment
#
#
# def payment_schedule(loan, rate, months):
#     user_monthly_payment = monthly_payment(loan, rate, months)
#     balance = loan
#     for month in range(1, months + 1):
#         i = rate / (100 * 12)
#         loan_in_month = balance * i
#         rest_loan = user_monthly_payment - loan_in_month
#         balance = balance - rest_loan
#         print(month, user_monthly_payment, balance)
#
#
# user_loan = float(input("Enter your loan:"))
# user_rate = float(input("Enter your rate:"))
# user_months = int(input("Enter your months:"))
#
# schedule = payment_schedule(user_loan, user_rate, user_months)



'''
🔹 8. Дострокове погашення
Функція early_repayment(loan, rate, months, extra_payment)
Завдання:
Додати щомісячний додатковий платіж
Порахувати:
новий термін кредиту
економію
'''

def monthly_payment(loan, rate, months):
    i = rate / (100 * 12)
    payment = loan * (i * (1 + i) ** months) / ((1 + i) ** months - 1)
    return payment


def early_repayment(loan, rate, months, extra_payment):
    user_monthly_payment = monthly_payment(loan, rate, months)
    balance = loan
    i = rate / (100 * 12)

    total_without_extra = user_monthly_payment * months
    total_with_extra = 0
    new_months = 0
    for month in range(1, months + 1):
        loan_in_month = balance * i
        rest_loan = user_monthly_payment - loan_in_month
        full_payment = user_monthly_payment + extra_payment

        balance = rest_loan - extra_payment
        total_with_extra += full_payment

        new_month = month

  # тут я остановился не знаю как продолжить.
  # была идею через цикл if но не знаю как его продолжить 


user_loan = float(input("Enter your loan: "))
user_rate = float(input("Enter your rate: "))
user_months = int(input("Enter your months: "))
user_extra_payment = float(input("Enter your extra payment: "))

user_payment = early_repayment(user_loan, user_rate, user_months, user_extra_payment)
print("Your early repayment is", user_payment)