import matplotlib.pylab as plt
from numpy import *

all_heightF = []
all_weightF = []
all_heightS = []
all_weightS = []
all_heightH = []
all_weightH = []

def drawWH(openfile):
    with open('./WHplot.txt', 'r+') as f:
        print('Parsing annotation files')

        for line in f:
            line_split = line.strip().split(',')
            (filename, height,weight, class_name) = line_split

            if class_name.encode('utf8') == 'Frieighter':
                all_heightF.append(height)
                all_weightF.append(weight)
            elif class_name.encode('utf8') == 'Ship':
                all_heightS.append(height)
                all_weightS.append(weight)
            elif class_name.encode('utf8') == 'MShip':
                all_heightH.append(height)
                all_weightH.append(weight)

        plt.scatter(all_weightF, all_heightF, color='blue', marker='x', label='Frieighter')
        plt.scatter(all_weightS, all_heightS, color='green', marker='o', label='Ship')
        plt.scatter(all_weightH, all_heightH, color='red', marker='^', label='MShip')
        plt.title('Recognization plot')
        plt.xlabel('Weight')
        plt.ylabel('Height')
        plt.legend(loc='upper right')
        plt.show()

all_XArea1 = []
all_XArea2 = []
all_XArea3 = []
all_YArea1 = []
all_YArea2 = []
all_YArea3 = []

def  drawArea(openfile):
    with open('./Aresplot.txt', 'r+') as f:
        print('Parsing annotation files')

        for line in f:
            line_split = line.strip().split(',')
            (filename, Area, class_name) = line_split

            if class_name.encode('utf8') == 'Frieighter':
                all_XArea1.append(Area)
                all_YArea1.append(0)
            elif class_name.encode('utf8') == 'Ship':
                all_XArea2.append(Area)
                all_YArea2.append(1)
            elif class_name.encode('utf8') == 'MShip':
                all_XArea3.append(Area)
                all_YArea3.append(2)

        plt.scatter(all_XArea1, all_YArea1, color='blue', marker='x', label='Frieighter')
        plt.scatter(all_XArea2, all_YArea2, color='green', marker='o', label='Ship')
        plt.scatter(all_XArea3, all_YArea3, color='red', marker='^', label='MShip')
        plt.title('Recognization Piexls')
        plt.xlabel('Areas')
        plt.ylabel('Types')
        plt.legend(loc='upper right')
        plt.show()

drawArea('./Aresplot.txt')