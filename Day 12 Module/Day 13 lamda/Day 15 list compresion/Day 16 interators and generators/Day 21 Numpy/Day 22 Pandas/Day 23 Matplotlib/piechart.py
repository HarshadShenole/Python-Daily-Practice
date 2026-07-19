import matplotlib.pyplot as plt
subject = ["Python","Java","C++"]
students = [40,35,25]
plt.pie(students,labels=subject, autopct = "%1.1f%%")
plt.show()