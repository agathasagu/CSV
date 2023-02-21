payrate = 10.0
paycheck = 0

while True:
    try:
        answer = float(input("How many hours did you work? "))
        paycheck = answer * payrate
        print(f"Your paycheck is ${paycheck:,.2f}")
        break
    except ValueError as err:
        # pass
        print("There was an error")  # does no go to the else

print("It is done")
