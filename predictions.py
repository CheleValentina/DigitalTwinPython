import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from ai_model import load_model


def feature_selection(data):
    # col_names = ["Date", "Active_Power", "Wind_Speed", "Theoretical_Power", "Wind_Direction"]
    # data = pd.read_csv("datasets/wind-turbine-scada-dataset/T1.csv", header=0, names=col_names)
    feature_cols = ["Wind_Speed", "Wind_Direction", "Theoretical_Power"]

    # Select features
    X = data[feature_cols]

    # Select target
    y = data.Active_Power

    return X, y


def data_splitting(X, y):
    # Divide data into 70% training and 30% testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1
    )
    return X_train, X_test, y_train, y_test


def linear_regression_model_building(X_train, X_test, y_train):
    # Create Decision Tree Classifier
    lr = LinearRegression()

    # Train the Decision Tree Classifier
    lr.fit(X_train, y_train)

    return lr


def model_evaluation(X_test, y_test, model, folder_name):
    y_pred = model.predict(X_test)

    print(f"Accuracy: {model.score(X_test, y_test)}")
    # The coefficients
    print("Coefficients: \n", model.coef_)
    # # The mean squared error
    print("Mean squared error: %.2f" % metrics.mean_squared_error(y_test, y_pred))
    # # The coefficient of determination: 1 is perfect prediction
    print("Coefficient of determination: %.2f" % metrics.r2_score(y_test, y_pred))

    print("Mean Absolute Error:", metrics.mean_absolute_error(y_test, y_pred))
    print("Mean Squared Error:", metrics.mean_squared_error(y_test, y_pred))
    print(
        "Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    )
    # plot prediction and actual data

    plt.clf()
    plt.plot(y_test, y_pred, ".")

    # plot a line, a perfit predict would all fall on this line
    x = np.linspace(0, 3500)
    y = x
    plt.plot(x, y)
    plt.savefig("plots/lr_model.png", transparent=True)


def get_prediction(wind_speed, wind_degree, theoretical_power):
    model = load_model()
    prediction = model.predict(
        np.array([[wind_speed, wind_degree, theoretical_power]])
    ).tolist()
    return prediction[0]
