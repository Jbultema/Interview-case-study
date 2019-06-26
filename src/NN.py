from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.model_selection import classification_report

import numpy as np
import pandas as pd


# baseline model
def create_baseline():
# create model
    model = Sequential()
    model.add(Dense(30, input_dim=155, kernel_initializer='normal', activation='linear'))
    #model.add(Dense(30, input_dim=60, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


if __name__ == "__main__":

    # import the cleaned data
    df = pd.read_excel("data/cleaned_interview_data.xls")
    df.drop(['Unnamed: 0'], axis= 1, inplace= True)

    # create the columns to use in models
    exclude_cols = ['expected_attendance_no','expected_attendance_yes', 'actual_attendance_yes', 'interview_date']
    include_cols = [x for x in df.columns.tolist() if x not in exclude_cols]
    y = df['actual_attendance_yes'].values
    X = df[include_cols].values

    # split the data into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # fix random seed for reproducibility
    seed = 7
    np.random.seed(seed)

    # evaluate model with standardized dataset
    estimator = KerasClassifier(build_fn=create_baseline, epochs=100, batch_size=5, verbose=1)
    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
    results = cross_val_score(estimator, X_train[:,:-1], y_train, cv=kfold)
    y_predicted = model.predict(X_test)
    test_score = classification_report(y_test, y_predicted)
    print("CV Results: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
    print("Classification report: \n", test_score)