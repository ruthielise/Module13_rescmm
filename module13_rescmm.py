#constraint 1: all caps and equals or less than 7 characters
symbol = input("What is the stock symbol? ")

if (symbol.isupper) :
    print("That input is not allowed. ")
elif (len(symbol) <= 7) :
    print("That input is not allowed. ")
else :
    print("Input accepted. ")

#constraint 2: must be one or two
chart_type = input("What chart type? ")

if (chart_type == "1" or chart_type == "2") :
    print("Input accepted. ")
else :
    print("That input is not allowed. ")

#constraint 3: must be between 1-4
time_series = input("What time series? ")

if (int(time_series) <= 4 or int(time_series) >= 1) :
    print("Input accepted. ")
else :
    print("That input is not allowed. ")

#constraint 4: must be in YYYY-MM-DD format
start_date = input("What is the start date? ")
numbers = start_date.split("-")
good_input = False

if (int(numbers[0]) >= 2024 or int(numbers[0]) <= 1962) :
    good_input = True
elif (int(numbers[1]) <= 12) :
    good_input = True
elif (int(numbers[1]) == 1 or int(numbers[1]) == 3 or int(numbers[1]) == 5 or int(numbers[1]) == 7 or int(numbers[1]) == 8 or int(numbers[1]) == 10 or int(numbers[1]) == 12) :
    if (int(numbers[2]) <= 31) :
        good_input = True
    else :
        good_input = False
elif (int(numbers[1]) == 4 or int(numbers[1]) == 6 or int(numbers[1]) == 9 or int(numbers[1]) == 11) :
    if (int(numbers[2]) <= 30) :
        good_input = True
    else :
        good_input = False
elif (int(numbers[1]) == 2) :
    if (int(numbers[2]) <= 28) :
        good_input = True
    else :
        good_input = False
else :
    good_input = False


#constraint 5: must be in YYYY-MM-DD format
end_date = input("What is the end date? ")
numbers = end_date.split("-")
good_input = False

if (int(numbers[0]) >= 2024 or int(numbers[0]) <= 1962) :
    good_input = True
elif (int(numbers[1]) <= 12) :
    good_input = True
elif (int(numbers[1]) == 1 or int(numbers[1]) == 3 or int(numbers[1]) == 5 or int(numbers[1]) == 7 or int(numbers[1]) == 8 or int(numbers[1]) == 10 or int(numbers[1]) == 12) :
    if (int(numbers[2]) <= 31) :
        good_input = True
    else :
        good_input = False
elif (int(numbers[1]) == 4 or int(numbers[1]) == 6 or int(numbers[1]) == 9 or int(numbers[1]) == 11) :
    if (int(numbers[2]) <= 30) :
        good_input = True
    else :
        good_input = False
elif (int(numbers[1]) == 2) :
    if (int(numbers[2]) <= 28) :
        good_input = True
    else :
        good_input = False
else :
    good_input = False