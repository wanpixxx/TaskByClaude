def main():
    temp = float(input("Enter temperature in Celsius: "))
    fahrenheit = (temp * 9/5) + 32
    return f"Temperature in Fahrenheit: {fahrenheit}"
print(main())
