# coding=utf-8
# sử dụng sort trường hợp đơn giản
arr = [1, 10, 2, 9, 8]
arr_asc = sorted(arr)
arr_desc = sorted(arr, reverse=True)
print('Ascending array: \n', arr_asc)
print('Descending array: \n', arr_desc)

arr = (1, 10, 2, 9, 8)
arr_asc = sorted(arr)
arr_desc = sorted(arr, reverse=True)
print('Ascending tuple: \n', arr_asc)
print('Descending tuple: \n', arr_desc)

# với dictionary khi apply sort thì sẽ apply trên key
dict_ = {1: '1', 10: '10', 2: '2', 9: '9', 8: '8'}
dict_asc = sorted(dict_)
dict_desc = sorted(dict_, reverse=True)
print('Ascending dictionary: \n', dict_asc)
print('Descending dictionary: \n', dict_desc)

# sort method(in-place sort) chỉ có cho object list
arr = [1, 10, 2, 9, 8]
print('Array before: \n', arr)
arr.sort()
print('Array after: \n', arr)
