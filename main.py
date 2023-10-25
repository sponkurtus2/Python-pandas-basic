import pandas as pd

data = {'col1': [1,2,3,4,6], 'col2': [2,5,6,7,2], 'col3': [9,8,1,4,5]}

data_frame = pd.DataFrame(data=data)

print(data_frame)

# Count number of columns
count_column = data_frame.shape[1]
print(f'Number of columns: {count_column}')

# Count number of rows
count_row = data_frame.shape[0]
print(f'Mimner of rows: {count_row}')