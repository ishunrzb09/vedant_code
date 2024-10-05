from validator import logValidator

x = {
    'weekdays' : 'short'
}

y = "MONDAY"



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = logValidator(x,y)
    return_value = obj.weekdaysValidator()
    print(return_value)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
