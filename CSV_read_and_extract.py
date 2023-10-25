import pandas as pd

# To open a file we use the following parameters
# 1 -> Name of the file
# 2 -> header=0 to show the first row (the titles)
# 3 -> sep=',' is used to indicate that the header row is separated by ,
Financial_data = pd.read_csv('SPY.csv', header=0, sep=',')
print(Financial_data.head())

# TIP: if we are working with large files, we can use the head() function
# To only show the 5 entries -> print(Financial_data.(head))

# Remove blank rows
# If our csv file has some blank rows, we can clean it with the following code
Financial_data.dropna(axis=0, inplace=True)


# Data categories
# We can analyze data and split it into 3 categories
# Numerical -> Numbers, which can be either discrete (1,4,5) or continuous (1,223, 3.5, 9.1093)
# Categorical -> Text like a color, a flavour, etc.
# Ordinal -> Values that can be compared, like for example sports, where Tennis is better than Soccer

# To start with, we can use the info() function to print the type of data our values have
print(Financial_data.info())

# We'll usually have object types, but we cand to analysis with that type
# so we'll convert that data into float64
# In the csv that we are using, our only object type is from the date
# And we shouln't turn the data to a float, so we'll just leave it that way
# But if we wanted to convert a data, we'd do it like this
'''
    Financial_data['Date'] = Financial_data['Date'].astype(float)
    print(Financial_data.info())
'''

# When our data is ready, we can start analyzing it
print(Financial_data.describe())
