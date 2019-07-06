import os
import csv
CH
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# List to store data 
Profits_losses = []
Dates = []
change = []
# Total_months = []
# Total = []
# Average_change = []
# Greatest_Increase_profits = []
# Greatest_Decrease_profits= []

# opening ressource data
with open(budget_data.csv, newline= " " , encoding='utf-8') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   cvs_header = next(csvfile)


for row in csvreader:
     # Run through the column
      Profits_losses.append(int(row[1]))
      Dates.append(row[0])
     
for rc in range(1,len(Profits_losses)):
       Change.append(int(Profits_losses[rc]) - int(Profits_losses[rc-1]))

# Determine the total number of months included in the dataset the total of months 
#  def average(Dates):
#     length = len(Dates)
 # Total_months = 0.0
    # for Date in Dates :
    #     Total_months += Dates
    # return Total_months / length

    
     # The average of the changes in "Profit/Losses" over the entire period
#  def average('Profits_losses'):
#     return sum ('Profits_losses') / len ('Profits_losses')
#           Average_change = average('Profits_losses')
#      # Determine the net total amount of "Profit/Losses" over the entire period
#      Total = 0.0
#     for Profits_losses in Profits_losses:
#        Total += Profits_losses
    #return Total / length
    # # The greatest increase in profits (date and amount) over the entire period
     Greatest_Increase_profits = min('Profits_losses')
    # # The greatest decrease in losses (date and amount) over the entire period
     Greatest_Decrease_profits= max('Profits_losses')

    # # Print an output list
     with open(output_path, 'w', newline='') as csvfile:

    # # Initialize csv.writer
     csvwriter = csv.writer(csvfile, delimiter=',')

     # Write the first row (column headers)
     csvwriter.writercolumn(['Date','Profits/Losses'])
    # writer.writerows(roster)
    # # Zip lists together
    # cleaned_csv = zip
    # Print result
    print(" the total Month : " + Total_months) 
    print("Total : " + Total) 
    print("Average change : " + round(Average_change, 1) )
    print("Greatest Increase in Profits : " + (0, Greatest_Increase_profits))
    print("Greatest Decrease in Profits : " + (0, Greatest_Decrease_profits))