yearofbirth = input("Enter your year of birth:")
difference = 2018 - int(yearofbirth)
if difference > 36:
    print('You are such an elder')
elif difference < 18:
    print('You are young')
else:
    print('You belong to the youth')