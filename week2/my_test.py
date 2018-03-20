
# for some_variable in range(0,10,2):
#     print(some_variable)



# if __name__ == "__main__":
print('test')

my_return_list = []

for counter in range(2):
    my_temporary_list = []
    for counter2 in range(2):
        to_append = "(i" + str(counter) + ", j" + str(counter2) + ")"
        my_temporary_list.append(to_append)

    print(to_append)
    my_return_list.append(my_temporary_list)
    

# print(my_return_list)




