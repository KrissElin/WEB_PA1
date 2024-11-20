main_list = [[1, 2, 3], [4, 5, 6]] 
main_list[0].append(7) # Добавляем число 7 в первый внутренний список 

del main_list[1][0] # Удаляем первый элемент 4 из второго внутреннего списка 
sum_first_list = sum(main_list[0])  # Сумма первого внутреннего списка 
sum_second_list = sum(main_list[1])  # Сумма второго внутреннего списка 
 
main_list[0].append(sum_first_list)  # Добавляем сумму в конец первого списка 
main_list[1].append(sum_second_list)  # Добавляем сумму в конец второго списка 
print(main_list)