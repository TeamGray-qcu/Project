import pandas as pd
import matplotlib.pyplot as plt

# Existing data
data1 = pd.DataFrame({
    'Pet ID': ['4466839344031767293', '4466839344031767293', '4466839344031767293', '4466839344031767293', '4466839344031767293'],
    'Gender': ['Female', 'Female', 'Female', 'Female', 'Female'],
    'Size': ['Large', 'Large', 'Large', 'Large', 'Large'],
    'Favorite': ['Chicken', 'Chicken', 'Chicken', 'Chicken', 'Chicken'],
    'Dry Food Orders': [21419.305, 18352.836, 36617.214, 18340.3, 14435.99],
    'Wet Food Orders': [0.0, 6624.0, 2901.9, 6624.0, 0.0],
    'Total Orders': [21419.305, 24976.836, 39519.114, 24964.3, 14435.99],
    'Order Payment Date': ['2019-04-11', '2019-04-11', '2019-04-11', '2019-04-11', '2019-04-11']
})

# Additional data
data2 = pd.DataFrame({
    'Pet ID': ['7813136397831853268', '7813136397831853268', '7986011032199863210', '7986011032199863210', '7711083807467252250'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Male'],
    'Size': ['Small', 'Small', 'Large', 'Large', 'Medium'],
    'Favorite': ['None', 'None', 'Mid', 'Mid', 'Superpremium'],
    'Dry Food Orders': [13412.369, 9987.614, 19421.485, 33418.72, 19109.84],
    'Wet Food Orders': [0.0, 0.0, 0.0, 0.0, 0.0],
    'Total Orders': [13412.369, 9987.614, 19421.485, 33418.72, 19109.84],
    'Order Payment Date': ['2020-01-02', '2019-12-01', '2019-12-27', '2019-09-09', '2019-09-09']
})

# Additional data 2
data3 = pd.DataFrame({
    'Pet ID': ['118114411501563384908', '18114411501563384908', '18114411501563384908'],
    'Gender': ['Female', 'Female', 'Female'],
    'Size': ['Medium', 'Medium', 'Medium'],
    'Favorite': ['Superpremium', 'Superpremium', 'Superpremium'],
    'Dry Food Orders': [10266.853, 17675.126, 17692.028],
    'Wet Food Orders': [0.0, 0.0, 0.0],
    'Total Orders': [10576.753, 17985.026, 18001.928],
    'Order Payment Date': ['2020-01-05', '2020-01-19', '2020-02-18']
})

# Additional data 3
data4 = pd.DataFrame({
    'Pet ID': ['16261514606242392388'],
    'Gender': ['Female'],
    'Size': ['Superpremium'],
    'Favorite': ['Medium'],
    'Dry Food Orders': [16163.431],
    'Wet Food Orders': [0.0],
    'Total Orders': [16163.431],
    'Order Payment Date': ['2020-01-30']
})

# Additional data 5
data5 = pd.DataFrame({
    'Pet ID': ['4466839344031767293'],
    'Gender': ['Female'],
    'Size': ['Large'],
    'Favorite': ['Chicken'],
    'Dry Food Orders': [0.0],
    'Wet Food Orders': [1.0],
    'Total Orders': [2.0],
    'Order Payment Date': ['2019-04-11']
})

# Additional data 6
data6 = pd.DataFrame({
    'Pet ID': ['4466839344031767293'],
    'Gender': ['Female'],
    'Size': ['Large'],
    'Favorite': ['Chicken'],
    'Dry Food Orders': [0.0],
    'Wet Food Orders': [1.0],
    'Total Orders': [1.0],
    'Order Payment Date': ['2019-04-11']
})

# Additional data 7
data7 = pd.DataFrame({
    'Pet ID': ['4466839344031767293'],
    'Gender': ['Female'],
    'Size': ['Large'],
    'Favorite': ['Chicken'],
    'Dry Food Orders': [0.0],
    'Wet Food Orders': [7.0],
    'Total Orders': [8.0],
    'Order Payment Date': ['2019-04-11']
})


data8 = pd.DataFrame({
    'Pet ID': ['4466839344031767293'],
    'Gender': ['Female'],
    'Size': ['Large'],
    'Favorite': ['Chicken'],
    'Dry Food Orders': [0.0],
    'Wet Food Orders': [3.0],
    'Total Orders': [4.0],
    'Order Payment Date': ['2019-04-11']
})


data9 = pd.DataFrame({
    'Pet ID': ['4466839344031767293'],
    'Gender': ['Female'],
    'Size': ['Large'],
    'Favorite': ['Chicken'],
    'Dry Food Orders': [0.0],
    'Wet Food Orders': [8.0],
    'Total Orders': [9.0],
    'Order Payment Date': ['2019-04-11']
})


data10 = pd.DataFrame({
    'Pet ID': ['4466839344031767293'],
    'Gender': ['Female'],
    'Size': ['Large'],
    'Favorite': ['Chicken'],
    'Dry Food Orders': [0.0],
    'Wet Food Orders': [0.0],
    'Total Orders': [6.0],
    'Order Payment Date': ['2019-04-11']
})


data11 = pd.DataFrame({
    'Pet ID': ['4466839344031767293'],
    'Gender': ['Female'],
    'Size': ['Large'],
    'Favorite': ['Chicken'],
    'Dry Food Orders': [0.0],
    'Wet Food Orders': [0.0],
    'Total Orders': [3.0],
    'Order Payment Date': ['2019-04-11']
})


data12 = pd.DataFrame({
    'Pet ID': ['4466839344031767293'],
    'Gender': ['Female'],
    'Size': ['Large'],
    'Favorite': ['Chicken'],
    'Dry Food Orders': [0.0],
    'Wet Food Orders': [0.0],
    'Total Orders': [9.0],
    'Order Payment Date': ['2019-04-11']
})


data13 = pd.DataFrame({
    'Pet ID': ['4466839344031767293'],
    'Gender': ['Female'],
    'Size': ['Large'],
    'Favorite': ['Chicken'],
    'Dry Food Orders': [0.0],
    'Wet Food Orders': [0.0],
    'Total Orders': [1.0],
    'Order Payment Date': ['2019-04-11']
})

# Concatenate the dataframes
data = pd.concat([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13], ignore_index=True)

# Convert Order Payment Date to datetime
data['Order Payment Date'] = pd.to_datetime(data['Order Payment Date'])


monthly_data = data.resample('M', on='Order Payment Date').sum()

# Plotting
plt.plot(monthly_data.index, monthly_data['Dry Food Orders'], marker='o', label='Dry Food Orders')
plt.plot(monthly_data.index, monthly_data['Wet Food Orders'], marker='o', label='Wet Food Orders')
plt.plot(monthly_data.index, monthly_data['Total Orders'], marker='o', label='Total Orders')

# Customize labels and title
plt.xlabel('Month')
plt.ylabel('Number of Orders')
plt.title('Orders Over Time')
plt.xticks(rotation=45)

# Show the plot
plt.legend()
plt.tight_layout()
plt.show()
