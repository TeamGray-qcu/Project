import pandas as pd
import matplotlib.pyplot as plt


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


data = pd.concat([data1], ignore_index=True)


data['Order Payment Date'] = pd.to_datetime(data['Order Payment Date'])


data_2019 = data[data['Order Payment Date'].dt.year == 2019]


monthly_data = data_2019.resample('M', on='Order Payment Date').sum()


plt.plot(monthly_data.index, monthly_data['Dry Food Orders'], marker='o', label='Dry Food Orders')
plt.plot(monthly_data.index, monthly_data['Wet Food Orders'], marker='o', label='Wet Food Orders')
plt.plot(monthly_data.index, monthly_data['Total Orders'], marker='o', label='Total Orders')


plt.xlabel('Month')
plt.ylabel('Number of Orders')
plt.title('Orders Over Time (2019)')
plt.xticks(rotation=45)


plt.legend()
plt.tight_layout()
plt.show()
