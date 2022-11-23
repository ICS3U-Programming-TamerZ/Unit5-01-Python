#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Nov. 22, 2022
# This program calculates the degrees fahrenheit with
# a given degrees celsius.


def TempConv():
    # Gets temperature celsius from User
    temp_cel_str = input("what is your temperature in degrees celsius ℃ : ")
    # Tries casting the temperature to a float
    try:

        temp_cel_float = float(temp_cel_str)
    # exception thrown if user did not enter a number
    except ValueError:
        print("Please enter a number")
    else:

        temp_fahrenheit_float = (temp_cel_float * 9 / 5) + 32
        print(f"{temp_cel_float}℃ = {temp_fahrenheit_float}℉")
    main()


def main():

    TempConv()


if __name__ == "__main__":
    main()
