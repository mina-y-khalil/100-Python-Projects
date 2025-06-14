# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # print(data)
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)
# print(data["temp"])
data_dict = data.to_dict()
# print(data_dict)
temp_list = data["temp"].to_list()
# print(temp_list)
average = round((sum(temp_list) / len(temp_list)), 2)
# print(average)
# print(data["temp"].mean()) #getting the average
# print(data["temp"].max())


#get data in columns
# print(data.condition)

#get data in rows
# print(data[data.day == "Monday"])

max_temp = data["temp"].max()
print(data[data.temp == max_temp])

