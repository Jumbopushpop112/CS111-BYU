import matplotlib.pyplot as plt
import random
random.seed(10)

# Simple plots
x_points = [1,2,3,4,5,6]
y_points = [1,4,9,16,25,36]
x2_points = [-3,-2,-1,0,1,2,3,4,5,6]
y2_points = [-27,-8,-1,0,1,8,27,64,125,216]

plt.plot(x_points, y_points)
plt.plot(x2_points, y2_points)

plt.show()
plt.clf()

# add colors
plt.plot(x_points, y_points, 'b')
plt.plot(x2_points, y2_points, 'r')

# add title and axis labels
plt.title("Squares and Cubes")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.clf()

# add legend
plt.plot(x_points, y_points, 'b', label="Squares")
plt.plot(x2_points, y2_points, 'r', label="Cubes")
plt.legend()

# change axis ranges
plt.xlim(0,8)
plt.ylim(-10, 300)

plt.savefig("squares.png")
plt.clf()

# Bar Plot
labels = ["M","T","W","Th","F","Sa","Su"]
values = [3,8,7,9,15,22,14]
plt.bar(labels, values, color="red")

plt.plot(x_points, y_points, 'b')

plt.clf()

# Histograms
numbers = [random.randrange(1,10) for i in range(100)]
print(numbers)
plt.hist(numbers)

plt.clf()

plt.hist(numbers, bins=9)

plt.clf()

bins = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
plt.hist(numbers, bins=bins)

plt.xticks([1,2,3,4,5,6,7,8,9])

plt.savefig("counts.png")
plt.clf()
