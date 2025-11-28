import matplotlib.pyplot as plt

# --- Input Section ---
while True:
    i=int(input('1. Expense Tracker\n2. Exit\nEnter your choice: '))
    if i==1:

      food = int(input('Enter your Food Expense = '))
      electricity_spend = int(input('Enter total unit of Electricity spend = '))
      charge_per_unit = int(input('Enter the charge per unit = '))
      rent = int(input('Enter your Hostel/Flat rent = '))
      total_person = 3  # or use input() for dynamic input
      
      # --- Calculation Section ---
      electricity_bill = electricity_spend * charge_per_unit
      total_amount = rent + food + electricity_bill
      output = total_amount // total_person
      
      print('\nEach person will pay:', output)
      print(f'\nBreakdown:\nRent = {rent}\nFood = {food}\nElectricity Bill = {electricity_bill}\n')
      
      # --- Visualization Section ---
      categories = ['Rent', 'Food', 'Electricity']
      values = [rent, food, electricity_bill]
      
      # Create a figure with 2 charts (1 row, 2 columns)
      plt.figure(figsize=(10, 5))
      
      # --- Bar Chart ---
      plt.subplot(1, 2, 1)
      plt.bar(categories, values, color=['#ff9999', '#66b3ff', '#99ff99'])
      plt.title('Hostel Expense Breakdown (Bar Chart)')
      plt.xlabel('Expense Type')
      plt.ylabel('Amount (₹)')
      plt.grid(True, linestyle='--', alpha=0.6)
      
      # --- Pie Chart ---
      plt.subplot(1, 2, 2)
      plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99'])
      plt.title('Expense Distribution (Pie Chart)')
      
      # --- Show both charts ---
      plt.tight_layout()
      plt.show()
    elif i==2:
        print('Exiting the program.')
        break
    else:
        print('Invalid choice. Please try again.')  
