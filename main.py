def display_as_percentage(val):
    return '{:.1f}%'.format(val * 100)


def calculate_simple_return(start_price, end_price, dividend=0):
    return (end_price - start_price + dividend) / start_price


# simple_return = calculate_simple_return(200, 250)
simple_return = calculate_simple_return(200, 250, 20)
# print("The simple rate of return is", display_as_percentage(
# simple_return))
# print("The simple rate of return is " + display_as_percentage(
# simple_return))
# print("The simple rate of return is {}".format(
# display_as_percentage(simple_return)))
# print("The simple rate of return is {0}".format(
# display_as_percentage(simple_return)))
print(f"The simple rate of return is "
      f"{display_as_percentage(simple_return)}")
