from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-&m-%d %H:%M:%S")
    print("current date and time: ," formatted_date)
display_current_datetime()

def calculate_future_date():
    number_of_days = int(input("Enter a number of days: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    formatted_future = future_date.strftime("%Y-&m-%d %H:%M:%S")
    print("future date: ," formatted_future)

calculate_future_date()



