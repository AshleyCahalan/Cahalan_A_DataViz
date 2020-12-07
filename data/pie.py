import matplotlib.pyplot as plt

value = [386, 239]
labels = ["Men", "Women"]
colors = ["green", "gold"]

explode = (0, 0.1)

plt.pie(value, labels=labels, colors=colors, explode=explode)
plt.show() # generate the pie chart