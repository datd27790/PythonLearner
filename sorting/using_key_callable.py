# xác định key tham gia vào quá trình sort
# khi thực hiện sort trên list các đối tượng phức tạp
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

# sort theo 2 tiêu chí: grade và age
# sử dụng lambda
print('--- USING lambda ---')
arr_asc = sorted(student_tuples, key=lambda x: (x[1], x[2]), reverse=True)
print('Array before: \n', student_tuples)
print('Array after: \n', arr_asc)
print()

# sử dụng itemgetter
print('--- USING itemgetter ---')
from operator import itemgetter, attrgetter

arr_asc = sorted(student_tuples, key=itemgetter(1, 2), reverse=True)
print('Array before: \n', student_tuples)
print('Array after: \n', arr_asc)
print()


# sử dụng attrgetter
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return '({0}, {1}, {2})'.format(self.name, self.grade, self.age)


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print('--- USING lambda on objects ---')
arr_asc = sorted(student_objects, key=lambda x: (x.grade, x.age), reverse=True)
print('Array before: \n', student_objects)
print('Array after: \n', arr_asc)
print()

print('--- USING attrgetter on objects ---')
arr_asc = sorted(student_objects, key=attrgetter('grade', 'age'), reverse=True)
print('Array before: \n', student_objects)
print('Array after: \n', arr_asc)
print()


s = sorted(student_objects, key=attrgetter('age'))
print(s)
s = sorted(s, key=attrgetter('grade'))
print(s)
