current_weather = str(input("What is the weather like today? (sunny/rainy/cold): "))
if current_weather == "sunny":
    message = "Wear a t-shirt and sunglasses."
elif current_weather == "rainy":
    message = "Don't forget your umbrella and a raincoat."
elif current_weather == "cold":
    message = "Make sure to wear a warm coat and a scarf."
else:
    message = "Sorry, I don't have recommendations for this weather."

print(message)
