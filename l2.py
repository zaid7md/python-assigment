#WAP a program that defines a list of countries that are a member of BRICS. Check weather a country ismember of BRICS or not
brics = ["russia" , "india" , "south africa" , "brazil"]
str = input("Enter the country's name : ")
if str in brics : 
    print("Yes this country is in brics ")
else:
    print("This country is not in brics")