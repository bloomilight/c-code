color_a=input("input the first color")
color_b=input("input the second color")
if color_a=="red" and color_b=="blue" or color_b=="red" and color_a=="blue":
   print("the secondary color is purple")
elif color_a=='yellow' and color_b=='blue' or color_b=='yellow' and color_a=='blue':
   print("the secondary color is green")
elif color_a=='red' and color_b=='yellow' or color_b=='red' and color_a=='yellow':
   print("the secondary color is orange")
else:
   print("the color you input is wrong")
