import pandas as pd
import matplotlib.pyplot as plt


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



data = pd.concat([data2, data3, data4], ignore_index=True)


data['Order Payment Date'] = pd.to_datetime(data['Order Payment Date'])


data_2020 = data[data['Order Payment Date'].dt.year == 2020]


monthly_data = data_2020.resample('M', on='Order Payment Date').sum()


plt.plot(monthly_data.index, monthly_data['Dry Food Orders'], marker='o', label='Dry Food Orders')
plt.plot(monthly_data.index, monthly_data['Wet Food Orders'], marker='o', label='Wet Food Orders')
plt.plot(monthly_data.index, monthly_data['Total Orders'], marker='o', label='Total Orders')


plt.xlabel('Month')
plt.ylabel('Number of Orders')
plt.title('Orders Over Time (2020)')
plt.xticks(rotation=45)


plt.legend()
plt.tight_layout()
plt.show()
