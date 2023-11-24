from pprint import pp


age = int(input("How old are you?\n"))
decades = int(age/10) # or age // 10 for int result directly
years = age % 10
pp("You are " + str(decades) + " decades and " + str(years) + " years old.")