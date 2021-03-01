import pandas as pd

facilityId = 'HUPP3050890'
quantity = 'Energi'
unit = 'kWh'
kind = 'Fjärrvärme'
complete_data = []
df = pd.read_excel('data-HUPP4001193.xlsx',engine='openpyxl',names=['Date','Value'])
for i in range(len(df['Date']) - 1):
    data_block = {}
    data_block = {'facilityId':facilityId,'quantity':quantity,'unit':unit,'kind':kind}
    data_block['startDate'] = df['Date'][i]
    data_block['endDate'] = df['Date'][i+1]
    data_block['value'] = df['Value'][i]
    complete_data.append(data_block)

# for i in range(10):
    # print(complete_data[i])

