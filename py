import ctypes
def main():
    temp = float(input("Enter temperature in Celsius: "))
    fahrenheit = (temp * 9/5) + 32
    if temp == 67 or temp == 69 or temp == 52:
       ctypes.windll.user32.MessageBoxW(0, f"ты все равнo eбlan, но градусы твои вот {fahrenheit}", "Ошiбка", 0x10)
    else:
        return f"Temperature in Fahrenheit: {fahrenheit}"
print(main())