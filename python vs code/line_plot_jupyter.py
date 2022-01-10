#import libraries
import seaborn as sns
import matplotlib.pyplot as plt

#load dataset
phool = sns.load_dataset("iris")
 
# change figure
plt.figure(figsize=(8,2))

#draw a line plot
sns.lineplot(x = "sepal_length", y ="sepal_width", data= phool)
plt.title("Phoolon ka Plot")
plt.xlim(2)
plt.ylim(1)
plt.show()