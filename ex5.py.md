```
my_name = "Zed A. Shaw"
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lba
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes,my_weight))
print("His teeth are usually %s depending on the coffee."% my_teeth)

# this line is tricky ,try to get it exactly right
print ("If I add %d ，%d,and %d I get %d." % (
    my_age,my_height,my_weight,my_age+my_height+my_weight))
```
#### python 格式化符
##### 先做再解释
---
#### 更多格式化符
#### 类型很多用法就一个
+ 整型数：%d
+ 无符号整型数：%u
+ 八进制：%o
+ 十六进制：%x   %X
+ 浮点数：%f
+ 科学记数法: %e   %E
+ 根据数值的不同自动选择%e或%f: %g
+ 根据数值的不同自动选择%E或%f: %G
