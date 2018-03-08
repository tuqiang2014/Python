cars = 100 #车的数量
space_in_a_car = 4.0 #每个车的空位
drivers = 30 #司机的数量
passengers = 90 #乘客个数
cars_not_driven =cars - drivers #计算不能开动的车数
cars_driven = drivers #计算可以开动车数
carpool_capacity = cars_driven * space_in_a_car #可承载乘客
average_passengers_per_car = passengers / cars_driven #每个车乘客数


print("There are",cars,"cars acailable.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")