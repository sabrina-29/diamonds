import pandas as pd 

diamonds=[]	
diamonds = pd.read_csv('diamonds.csv')
print(diamonds.head())

max_price = diamonds['price'].max()
print(max_price)

avg_price = diamonds['price'].mean()
print(avg_price)


cut_counts = diamonds['cut'].value_counts()
print(cut_counts)


color_counts = diamonds['color'].value_counts()
print(color_counts)

meidan_carat = diamonds['carat'].median()
print(meidan_carat)


for cut in diamonds['cut'].unique():
		def avg_carat_cut(cut):
			return diamonds[diamonds['cut']==cut]['carat'].mean()
		print(cut, avg_carat_cut(cut))


for color in diamonds['color'].unique():
	def avg_price_cut(cut):
		return diamonds[diamonds['color']==cut]['price'].mean()
	print(color, avg_price_cut(color))





