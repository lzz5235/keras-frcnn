import matplotlib.pylab as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import MultipleLocator
from numpy import *

widths = []
lengths = []
recogs = []
amoungs = []

areas = []
rates = []

def  drawplot():
    with open('./point.txt', 'r+') as f:
        print('Parsing annotation files')

        for line in f:
            line_split = line.strip().split(',')
            (width, length, recog, amoung) = line_split

            widths.append(int(width))
            lengths.append(int(length))
	    areas.append(int(width)*int(length))
            recogs.append(float(recog))
            amoungs.append(float(amoung))
            rates.append(float(recog)/float(amoung))     

        plt.plot(areas, rates, color='red', linestyle='-', marker = 's',linewidth = 1.5, markersize=5)
	plt.gca().yaxis.set_major_locator(MultipleLocator(0.05))
	plt.gca().xaxis.set_major_locator(MultipleLocator(5000))
	plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
	#plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('12x23'))
        plt.title('Template resolution analysis')
        plt.xlabel('Piexls')
        plt.ylabel('AP')
	plt.legend()
        plt.grid()
        plt.show()

drawplot()
