# TODO Найдите количество книг, которое можно разместить на дискете
book_bytes = 100*50*25*4
disk_bytes = 1.44*1024*1024
amount = int(disk_bytes//book_bytes)
print("Количество книг, помещающихся на дискету:", amount)
