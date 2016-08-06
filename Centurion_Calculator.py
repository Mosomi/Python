import datetime    #get tle date libraries from python rep
get = datetime.datetime.now()
name = input("Kindly Enter your Name:\n")
age = int(input("Please enter your Age:\n"))
currYear = get.year
centurion = ((100-age)+currYear)
print ("""Hello %r. Your current age is %r and you will turn 100 in year %r\n"""
%(name,age,centurion))
