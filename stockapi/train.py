import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import os


from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV, train_test_split
from stockapi import model_train

def TrainModel(dataTobeRetrained):
    final_df = pd.read_csv("stockapi/original_data.csv")
    print(final_df.head(3))
    print(final_df.columns)
    final_df=final_df.dropna()

    if dataTobeRetrained != None:
        if len(dataTobeRetrained) > 0:
            dataTobeRetrained["Weekday"]=dataTobeRetrained['UpdatedDates'].dt.weekday
            dataTobeRetrained["WeekdayName"]=dataTobeRetrained['Weekday'].map({
                0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
                4: 'Friday', 5: 'Saturday', 6: 'Sunday'
            })
            final_df = pd.concat(final_df,dataTobeRetrained)

    #final_df = final_df.rename(columns={'Date ':'Date', 'Open ':'Open', 'High ':'High', 'Low ':'Low', 'Close ':'Close', 'Shares Traded ':'Shares Traded','Turnover (₹ Cr)':'Turnover'})
    original=final_df.copy()

    original=original.sort_values(by="UpdatedDates", ascending=True)
    original['Target'] = (original['Close'].shift(-1) > original['Close']).astype(int)

    # Drop the last row since it will have a NaN in the 'Target' column
    original = original.dropna()

    best_model=model_train.generateModel(original)
    best_model.save_model('stock_api_model.json')


def getPredictions(dictParams):

    # Load model from file
    absolute_path = os.path.dirname(__file__)
    print(absolute_path)
    best_model = XGBClassifier()
    x=os.getcwd()+"/stock_api_model.json"
    print(x)
    best_model.load_model(x)

    new_data = pd.DataFrame(dictParams)
    # Make predictions using the trained model
    predictions = best_model.predict(new_data)

    if predictions[0] == 0:
        print("NIFTY will go down")
        return 0
    elif predictions[0] == 1:
        print("NIFTY will go up")
        return 1



