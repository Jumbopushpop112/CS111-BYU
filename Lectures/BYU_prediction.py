import matplotlib.pyplot as plt
import numpy as  np

# Set each of these variables to a list of BYU scores 
# and corresponding Opponent scores, respectively
# You can get the scores here: rp=EgZjaHJvbWUqBggAhttps://www.google.com/search?q=byu+football+schedule&rlz=1C1GCEA_enUS1167US1167&oq=byu+foot&gs_lcEEUYOzIGCAAQRRg7MgYIARBFGDkyBggCEEUYQDIGCAMQRRg7MgYIBBBFGDvSAQg0MDg1ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8#sie=t;/m/026l1lq;6;/m/012hfxch;mt;fp;1
x_points = [69,27,34,24,38,33,24,41,7,44,26] #byu scores
y_points = [0,3,13,21,24,27,21,27,29,13,14]
x_points.sort()
y_points.sort()
# Now call the plt.scatter() method with x_points, y_points, and
# label="Scores" as the three parameters
plt.scatter(x_points,y_points,label="Scores")
# Now add a title, an xlabel, and a ylabel to the plot
plt.title("BYU Scores")
plt.xlabel("BYU Scores")
plt.ylabel("Opponenet Scores")
# Now create a trendline. Can you tell what each of these numpy methods is doing?
coefficients = np.polyfit(x_points,y_points,1)
print(coefficients)
p = np.poly1d(coefficients)
print(p)
x_fit = np.linspace(7,69)
print(x_fit)
y_fit = p(x_fit)
print(y_fit)

# Now plot the trendline using x_fit and y_fit as the lists of x and y points
# also make the line red and label it as "Trendline"
plt.plot(x_fit,y_fit,"r",label="Trendline")
# Add a legend and show the plot
plt.legend()
plt.show()
