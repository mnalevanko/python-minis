def even_numbers(list_of_numbers, limit):
    return list(filter(lambda x: x %2 == 0, list_of_numbers))[:limit]

print(even_numbers([1,2,3,4,5,6,7,8,9], 20))
