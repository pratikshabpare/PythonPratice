# def generate_numbers(limit):
#     for num in range(1,limit+1):
#         yield num
# sequence=generate_numbers(5)
# for value in sequence:
#     print(value)
# def number_generator():
#     numbers=[1,2,3]
#     for num in numbers:
#         yield num
# for item in number_generator():
#     print(item)
def calculate_total():
    value=[1,2,3]
    result=sum(value)
    return result
output=calculate_total()
print(output)