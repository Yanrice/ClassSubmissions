import os
import csv



# opening ressource data
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# List to store data 
Profits_losses = []
Dates = []
changes = []
# Total_months = []
count_budget = 0 
total_profit = 0
initial_profit = 0
# Average_change = []
# Greatest_Increase_profits = []
# Greatest_Decrease_profits= []
# Open and read csv
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csvreader:
  # count number of month 
    count_budget = count_budget + 1
  # Run through the column
  Profits_losses.append(int(row[1]))
  Dates.append(row[0])
  total_profit = total_profit + int(row[1])
 # average change in profits month after month
  Final_profit = int(row[1])
  profit_monthly_change = Final_profit - initial_profit
      
     # Define the monthly change
  changes.append(profit_monthly_change) 

  profit_total_change = profit_total_change + profit_monthly_change
  initial_profit = Final_profit
  # Determine the total number of months included in the dataset the total of months 
  def average(Dates):
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

    # Determine the average change in profits
profits_average_change = (profit_total_change/count_budget)

    # # The greatest increase in profits (date and amount) over the entire period
Greatest_Increase_profits = min('Profits_losses')
    # # The greatest decrease in losses (date and amount) over the entire period
Greatest_Decrease_profits= max('Profits_losses')

Increase = Dates[changes.index(Greatest_Increase_profits)]
Decrease = Dates[changes.index(Greatest_Decrease_profits)]

    # # Print an output list
    # with open(output_path, 'w', newline='') as csvfile:

    # # Initialize csv.writer
    # csvwriter = csv.writer(csvfile, delimiter=',')

     # Write the first row (column headers)
    # csvwriter.writercolumn(['Date','Profits/Losses'])
    # writer.writerows(roster)
    # # Zip lists together
    # cleaned_csv = zip
    # Print result
   print("Financial Analysis")
   print("--------------------------------------------")
   print(" Total Months : " + str(count_budget)) 
   print("Total : " + str(total_profit)) 
   print("Average change : " + "$" + str( profits_average_change))
   print("Greatest Increase in Profits : " + str(Increase) + "$" + (0, Greatest_Increase_profits))
   print("Greatest Decrease in Profits : " + (0, Greatest_Decrease_profits))