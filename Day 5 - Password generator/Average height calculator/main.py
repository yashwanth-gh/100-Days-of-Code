# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
heighttotal=0
count=0
for height in student_heights:
    heighttotal+=height
    count+=1
avgheight=heighttotal/count
print(round(avgheight))




