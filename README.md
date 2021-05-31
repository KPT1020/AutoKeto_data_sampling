# AutoKeto_data_sampling

This project include the codes and sampled data before 30/5.
Currently in the file, sampling frequency of 10 , 1000,6000 Hz is tested and recorded
On 31/5

To use the codes is simple:
1.load your data starting from cell B2 in excel file
2. ADD column header Time and Reading at column A and B
3. Save your data to be visualized in .csv format in excel
4. Drag your saed .csv into vs code where your codes are located.
5. Copy relative part by right clicking the .csv file
6. paste the relative path to your code, which is data= pd.read_csv('xxxxxxxxxxxxxxxxx')
7. run the code

The above procedure will return two things
1. standard deviation of the data set
2. moving average of the data set
3. upper and lower limit of the moving average with error of +/- s.d.

You may want to change some grpah property such as the thickness of line and colour, please refer to the matplotlib documentation
https://matplotlib.org/

Feel free to create extra functions to optimize the data visualization

Francis words:)
