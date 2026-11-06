import matplotlib.pyplot as plt
apple_prices = [150, 155, 160, 165, 170]
mango_prices = [100, 105, 110, 115, 120]
year1=[2018, 2019, 2020, 2021, 2022]
yaer2=[2018, 2019, 2020, 2021, 2022]
plt.bar(year1, apple_prices, color='orange', label='Apple Prices', width=0.4)
plt.bar(yaer2, mango_prices, color='lightgreen', label='Mango Prices', width=0.4)
plt.legend()
plt.xlabel('Year')
plt.ylabel('Prices')
plt.grid(True, color='gray')
plt.title('Market Info')
plt.show()