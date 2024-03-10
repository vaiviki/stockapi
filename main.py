from stockapi import train, model_train
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#This function will train the model
def train_model():
    train.TrainModel(None)
    
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    train_model()
    pred_params={
    'Open': [22505.30],
    'High': [22525.65],
    'Low': [22430.00],
    'Close': [22493.55],
    'Shares Traded': [379865142],
    'Turnover': [33558.65],
    'Weekday':[3]}
    train.getPredictions(pred_params)
    


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Welcome to Stock Market API')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
