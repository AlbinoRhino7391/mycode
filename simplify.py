#!/usr/bin/env python3

""" Simple program to tell the user what their chinese zodiac sign is"""
def main():
    zodiac_signs = {
        (2011, 1999, 1987, 1975, 1963): "Rabbit",
        (2020, 2008, 1996, 1984, 1972, 1960): "Rat",
        (2010, 1998, 1986, 1974, 1962): "Tiger",
        (2021, 2009, 1997, 1985, 1973, 1961): "Ox",
        (2012, 2000, 1988, 1976, 1964): "Dragon",
        (2013, 2001, 1989, 1977, 1965): "Snake",
        (2014, 2002, 1990, 1978, 1966): "Horse",
        (2015, 2003, 1991, 1979, 1967): "Sheep",
        (2016, 2004, 1992, 1980, 1968): "Monkey",
        (2017, 2005, 1993, 1981, 1969): "Rooster",
        (2018, 2006, 1994, 1982, 1970): "Dog",
        (2019, 2007, 1995, 1983, 1971): "Pig"
    }

    usr_name = input("Please enter your name:\n>")
    usr_name = usr_name.title()
    usr_date = int(input("Please enter your birth year in YYYY format, e.g., 2010:\n>"))

    for years, sign in zodiac_signs.items():
        if usr_date in years:
            print(f"{usr_name} your zodiac sign is {sign}.")
            break
    else:
        print("Invalid birth year or zodiac sign not found.")

if __name__ == "__main__":
    main()
