import pandas as pd
first = pd.read_csv("online data.csv")
print(first)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
                                                                                                          
f= sns.countplot(x="Region", hue="Rep", data=first)
plt.show()
