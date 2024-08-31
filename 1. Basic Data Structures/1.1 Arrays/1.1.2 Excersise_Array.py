# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out:
#   1. In Feb, how many dollars you spent extra compare to January?
#   2. Find out your total expense in first quarter (first three months) of the year.
#   3. Find out if you spent exactly 2000 dollars in any month
#   4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#   5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

monthExpense = {
    "January": 2200,
    "February": 2350,
    "March": 2600,
    "April": 2130,
    "May": 2190
}

febDifJan = monthExpense["February"] - monthExpense["January"]
print(f'1. In Feb, how many dollars you spent extra compare to January?\n', febDifJan)

trimester = monthExpense["January"] + monthExpense["February"] + monthExpense["March"]
print(f'2. Find out your total expense in first quarter (first three months) of the year:\n', trimester)

def exactlyAmount():
    found = False
    for value in monthExpense.values():
        if value == 2000:
            month_val = list(monthExpense.keys())[list(monthExpense.values()).index(value)]
            print(month_val)
            found = True
            break
    if not found:
        print('No month found with this amount')

print('3. Find out if you spent exactly 2000 dollars in any month:') 
exactlyAmount()

print('4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list')
monthExpense.update({"June": 1980})

refundApril = monthExpense["April"] + 200
print(f'5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this:\n', refundApril)




    
