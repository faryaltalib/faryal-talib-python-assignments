import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks" , color_codes=True)

titanic = sns.load_dataset("titanic")
sns.catplot(x='sex', y='survived', hue='class', kind='point', data=titanic)
plt.show()


#theme means style and color of graphs
