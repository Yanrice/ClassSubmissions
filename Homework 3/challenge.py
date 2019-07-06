# First the variables are defined 
# price as a float
# percentage_tip as a float
# Total_price as a float
# Number_of_people as int

# The user's input for the prompt.
price = float(input(" the value of the bill is "))
# The user's input for the desired percentage of the tip
percentage_tip  = float(input(" the desired tip percentage is "))
# the user input how many people are splitting the tip
Number_of_people = int(input(" How many people are splitting the tip "))
# The amount paid by people splitting the bill
tip_split = ((percentage_tip * price)/100) / Number_of_people
    
# using percent tip, let calculate to finale price
Total_price = (price + ((percentage_tip * price)/100)) 
"${:2f}".format (Total_price)
# Prints a statement adding the variable
print("The Total price is " + str(Total_price))
print("The amount paid by each person spliting the tip is " + str(tip_split))

# math.ceil(tip_split*100)/100

