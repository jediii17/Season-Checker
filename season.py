print("\nSEASON APPLICATIONS\nUse numbers 1-12 for months, and 1-31 for days.")

m = int(input("\nInput month: "))
day = int(input("Input day: "))
print(" ")

# Months And Temperatures
if m == 1:
    month = 'January'
    C = '0'
    Description = 'the freezing point of water'
elif m == 2:
    month = 'February'
    C = '0'
    Description = 'the freezing point of water'
elif m == 3:
    month = 'March'
    C = '10'
    Description = 'a cool day'
elif m == 4:
    month = 'April'
    C = '10'
    Description = 'a cool day'
elif m == 5:
    month = 'May'
    C = '21'
    Description = 'the room temperature'
elif m == 6:
    month = 'June'
    C = '30'
    Description = 'a beach weather'
elif m == 7:
    month = 'July'
    C = '30'
    Description = 'a beach weather'
elif m == 8:
    month = 'August'
    C = '37'
    Description = 'the body temperature'
elif m == 9:
    month = 'September'
    C = '30'
    Description = 'a cool day'
elif m == 10:
    month = 'October'
    C = '21'
    Description = 'the room temperature'
elif m == 11:
    month = 'Novermber'
    C = '10'
    Description = 'a cool day'
elif m == 12:
    month = 'December'
    C = '0'
    Description = 'the freezing point of water'
elif m > 12:
    month = 'INPUT ERROR'
    C = 'INPUT ERROR'
    Description = 'INPUT ERROR'

# Seasons
if month in ('January', 'February', 'March'):
    s = 'Winter Season'
elif month in ('April', 'May', 'June'):
    s = 'Spring Season'
elif month in ('July', 'August', 'September'):
    s = 'Summer Season'
elif month in ('October', 'November', 'December'):
    s = 'Fall Season'

elif (month == 'March') and (day > 15):
    s = 'Spring Season'
elif (month == 'June') and (day > 15):
    s = 'Summer Season'
elif (month == 'September') and (day > 15):
    s = 'Fall Season'
elif (month == 'December') and (day > 15):
    s = 'Winter Season'

elif (month == 'INPUT ERROR'):
    s = 'INPUT ERROR'

# Ascii
if s == 'Winter Season':
    print("       ,---------------------------------.    ,-- ")
    print("       |,-------------------------------.|    |,- ")
    print("       || o      /\  o     o       o    ||    ||  ")
    print("   ,--.||    o  /  \    o             o ||    ||o ")
    print("-. \    `. o   /-..-\         o       ,-:|    ||  ")
    print("  \ )    _\  /\/    \     o          :   \    ||")
    print("   )),;;'(. /  \  o  \o           o  |    )   ||")
    print("  / ((.`   >/`'\.__..-\/\    /\      |   /    ||")
    print("  \  ))   ")
elif s == 'Spring Season':
    print(" ,-.")
    print("/ \_/ \ ")
    print(">-(_)-<")
    print("\_/ \_/")
    print("  `-'  ")
elif s == 'Summer Season':
    print("     \     |     /")
    print("       \       /")
    print("         ,d8b,           ., ")
    print(" (')-')_ 88888 ---   ;';'  ';'. ")
    print("('-  (. ')98P'      ';.,;    ,; ")
    print(" '-.(   )'     \       '.';.' ")
    print("           |     \ ")
    print("           | ")
elif s == 'Fall Season':
    print("     .\^/.  ")
    print("   . |`|/| . ")
    print("   |\|\|'|/| ")
    print(".--'-\`|/-''--. ")
    print(" \`-._\|./.-'/   ")
    print("  >`-._|/.-'< ")
    print(" '|/~~|~~\|' ")
    print("       | ")

print(f'\nIt is {month} {day} and it is {s}.')
print(f'The temperature is {C} degrees Celsius and it is {Description}.\n')
