#steps involoved in data visualization

#step-1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt

#step-2 set a theme
sns.set_theme(style="ticks", color_codes=True)

#step-3 import data sets...you can also import your own data
kashti = sns.load_dataset("titanic")

# #step-4 plot basic graph with 1 vairable
# f= sns.countplot(x= "sex", data= kashti)
# plt.show()0

# #step-5 plot basic graph with 2 variables or subgroups or classes
# f= sns.countplot(x= "sex", data= kashti, hue= "class")
# plt.show()

#step-6 plot basic graph with titles
f= sns.countplot(x= "sex", data= kashti, hue= "class")
f.set_title("My first count plot--yeyyyyyyyyyy")
plt.show()