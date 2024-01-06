# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()


# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#
#             temperatures.append(int(row[1]))
# print(temperatures)
import pandas

# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data["temp"] == data["temp"].max()])
# data_dict = {
#     "students": ["Amy", "Bernardo", "Angela"],
#     "scores": [76, 100, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = 0
red = 0
black = 0
for colors in data["Primary Fur Color"]:
    if colors == "Gray":
        gray += 1
    elif colors == "Cinnamon":
        red += 1
    elif colors == "Black":
        black += 1
print(gray, red, black)
squirrel = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, red, black]
}
squirrel = pandas.DataFrame(squirrel)
squirrel.to_csv("squirrel_count.csv")
