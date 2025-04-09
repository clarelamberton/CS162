import matplotlib.pyplot as plot
# set up your lists
numlist = [20, 16, 14, 10]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['y', 'm', 'c', 'r' ]
explodelist = [0.3, 0.0, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 60)
plot.axis('equal')
plot.savefig('piechart.png')

