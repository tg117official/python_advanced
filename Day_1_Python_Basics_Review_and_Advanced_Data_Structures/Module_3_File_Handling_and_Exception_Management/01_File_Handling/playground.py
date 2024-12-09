
file = open(r'C:\Users\Sandeep\Desktop\data\cr.txt', 'a')
file.write("I am loving python")
file.close()

with open(r'C:\Users\Sandeep\Desktop\data\cr.txt', 'a') as file :
    file.write("I am loving python")

print("Next Steps")