numbers = [1,4,5,6,2,15,11,2,4,9,8]

a = int(input('Введите число: '))

print('Такое число есть в списке' if numbers.count(a) else 'Такого числа нет в списке')