destination = input("Enter your destination")
distance = float(input("enter the distance"))
ave_speed = float(input("Enter average speed in km\h"))

time = (distance // ave_speed)

print(f"Destination: {destination}")
print(f"Distance: {distance} km")
print(f"Average Speed: {ave_speed}  km/h")
print(f"Estimated Travel Time: {time} hours")