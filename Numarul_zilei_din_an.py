"""
Se verifica daca anul este bisect. Un an este bisect daca este divizibil cu 4
Insa daca este divizibil cu 100 nu este an bisect decat daca este divizibil si cu 400
"""
def an_bisect(year):
    """
      Verifica daca anul introdus de la tastatura este bisect sau nu

      Parameters:
      -----------
      year : int
          Valoare introdusa de la tastatura, reprezentand anul

      Returns:
      --------
      boolean : True daca este an bisect, False daca nu este bisect

      Examples:
      ---------
      print(an_bisect(2024))
    """
    while year % 4 == 0 and year % 100 == 0:  # Se verifica daca anul este divizibil cu 4 si cu 100
        if year % 400 == 0:  # Se verifica daca este divizibil si cu 400
            return True
        else:
            return False
    else:
        # Se verifica daca este divizibil doar cu 4 si returneaza True sau False in functie de rezultat
        if year % 4 == 0:
            return True
        else:
            return False


def generate_day(month, day):
    # Se verifica daca luna introdusa este Ianuarie, daca este se afiseaza direct ziua
    if month == 1:
        print(day)
    else:

        result = 0

        for i in range(1, month):
            # Se verifica daca luna are 31 de zile si se aduna 31 la result
            if i in (1, 3, 5, 7, 8, 10, 12):
                result += 31
            # Se verifica daca luna are 30 de zile si se aduna 30 la result
            elif i in (4, 6, 9, 11):
                result = result + 30
            else:
                # Se verifica daca anul este bisect si aduna 29 daca este sau 28 daca nu
                if an_bisect(year_input) is True:
                    result += 29
                else:
                    result += 28

        result += day

        return result


# Invocare cu argumente de la tastatură
year_input = int(input("year:"))
month_input = int(input("month: "))
day_input = int(input("day: "))
print("Ziua cu numarul:", generate_day(month_input, day_input))
print("Anul este bisect?", an_bisect(year_input))