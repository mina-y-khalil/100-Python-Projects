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

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# average = round((sum(temp_list) / len(temp_list)), 2)
# print(average)
# print(data["temp"].mean()) #getting the average
# print(data["temp"].max())


#get data in columns
# print(data.condition)

#get data in rows
# print(data[data.day == "Monday"])

# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250613.csv")
gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dic = {
    "Fur Count" : ["Gray" , "Cinnamon" , "Black"],
    "Count" : [gray_squirrel_count , cinnamon_squirrel_count , black_squirrel_count]
}

df = pandas.DataFrame(data_dic)
df.to_csv("squirrel_count.csv")


