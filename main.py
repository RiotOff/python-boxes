from time import sleep

firstbox = '5 бутылок' # Что находится в первой коробке
secondbox = '10 консерв' # Что находится в другой коробке

sleep(2)

# Спрашиваем про первую коробку
firstbox2 = input('Вы хотите узнать, что находится в первой коробке? (Да / Нет): ')

sleep(2)

# Если ответ равен 'да'
if firstbox2.lower() == 'да':
	sleep(2)
	print(f'В первой коробке находится {firstbox}!')
else: # Исключение
	sleep(2)
	print('Тогда...')

sleep(2)

# Спрашиваем про другую коробку
secondbox2 = input('Вы хотите узнать, что находится в другой коробке? (Да / Нет): ')

# Если ответ равен 'да'
if secondbox2.lower() == 'да':
	sleep(2)
	print(f'В другой коробке находится {secondbox}!')
else: # Исключение
	sleep(2)
	print('Мне больше нечего вам сказать! :(')