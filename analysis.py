import pandas as pd 
from matplotlib import pyplot as plt 

top_500_albums = pd.read_csv("2020RollingStoneTop500Albums.csv")

album_release_year = top_500_albums['ReleaseYear']

plt.hist(album_release_year, range=(1950, 2019), bins=10, edgecolor='black')
plt.title("Top 500 Albums, By Decade")
plt.xlabel("Decade")
plt.ylabel("Count")

plt.show()
