1. Написать декоратор, который проверяет, что все аргументы (как позиционные, так и именованные) 
   исходной функции являются итерируемыми объектами. 
   
    В случае ошибки выводить сообщение какой аргумент не является итерируемым: 
    
```python
raise TypeError("Объект <название или номер позиционного аргумента> <значение аргумента> не является итерируемым")
```

Для проверки итерируемости можно использовать выражение генератор
```python
(_ for _ in some_obj)
```