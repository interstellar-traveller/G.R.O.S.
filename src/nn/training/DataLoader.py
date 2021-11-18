import numpy as np
import matplotlib.pyplot as plt
from numpy.core.arrayprint import array_repr

class DataLoader():
    def __init__(self, file_path, mode='r'):
        """initialize a data loader

        Args:
            file_path (str): path of the original data file
            mode (str, optional): mode to open the file. Defaults to 'r'.
        """
        self.path = file_path
        self.mode = mode
        
    def read_file(self):
        """read file into the data loader according to the path

        Returns:
            file (txt): the txt format data file
        """
        return open(self.path, self.mode)
    
    def formatting(self):
        """reformat the data stored in the data file into numpy array with suitable dimensions

        Returns:
            array (ndarray): a numpy array with suitable dimensions of (n, 21, 3)
        """
        self.file = self.read_file()
        array = np.loadtxt(self.file)
        array.resize(int(array.shape[0]/21),21,3)
        # print(array)
        return array
        
    def arr_shape(self):
        """give out the shape of the formatted array

        Returns:
            array shape (arr): the shape of the formatted numpy array
        """
        return self.formatting().shape
    
    def visualize(self, serial_num):
        """visualize a given data set (data points arranged in a hand's shape)

        Args:
            serial_num (int): determines which data set to be visualized
        """
        data_set = self.formatting()[serial_num]
        x = [item[1] for item in data_set]
        y = [item[2] for item in data_set]
        plt.scatter(x, y)
        plt.gca().invert_yaxis() 
        plt.show()
    
# dl = DataLoader('palmdata.txt', 'r')
# dl.visualize(0)
# print(dl.arr_shape())
