import pandas as pd

import graphics
import predictions
import pickle

from ai_model import save_model

data = pd.read_csv("datasets/wind-turbine-scada-dataset/T1.csv")
folder_name = 'plots'


def initialize_data(data):
    data['Date/Time'] = pd.to_datetime(data['Date/Time'])
    data.set_index('Date/Time', inplace=True)

    data.columns = ["Active_Power", "Wind_Speed", "Theoretical_Power", "Wind_Direction"]
    graphics.plot_data_statistics(data, folder_name + '/describe_data.png')

    data["Loss"] = data["Theoretical_Power"] - data["Active_Power"]


def resample_data(data):
    hourly = pd.DataFrame()
    daily = pd.DataFrame()
    weekly = pd.DataFrame()
    monthly = pd.DataFrame()

    for col in data.columns:
        weekly[col] = data[col].resample('W').mean()

    for col in data.columns:
        monthly[col] = data[col].resample('M').mean()

    for col in data.columns:
        daily[col] = data[col].resample('D').mean()

    for col in data.columns:
        hourly[col] = data[col].resample('H').mean()

    return hourly, daily, weekly, monthly


def plot_analysis_graphics(date, date_nm, data, data_nm):
    hourly, daily, weekly, monthly = date
    hourly_nm, daily_nm, weekly_nm, monthly_nm = date_nm

    graphics.plot_data_information(data_nm, folder_name + '/sample_of_data.png')

    graphics.plot_loss(hourly, folder_name + "/loss_before_maintenance")
    graphics.plot_loss(hourly_nm, folder_name + "/loss_after_maintenance")

    graphics.plot_power_by_date(hourly_nm, folder_name + '/power.png')
    graphics.plot_power_daily_monthly(monthly_nm, weekly_nm, folder_name + '/power_daily_monthly.png')

    graphics.plot_speed_power_relation(data, folder_name)
    graphics.plot_data_distribution(data, folder_name)


if __name__ == '__main__':
    initialize_data(data)
    hourly, daily, weekly, monthly = resample_data(data)

    # Remove maintenance values
    data_nm = data[~((data['Active_Power'] <= 0) & (data['Wind_Speed'] > 3.3))]
    hourly_nm, daily_nm, weekly_nm, monthly_nm = resample_data(data_nm)

    X, y = predictions.feature_selection(data_nm)
    X_train, X_test, y_train, y_test = predictions.data_splitting(X, y)
    model = predictions.linear_regression_model_building(X_train, X_test, y_train)
    predictions.model_evaluation(X_test, y_test, model, folder_name)

    save_model(model)

    plot_analysis_graphics(
        (hourly, daily, weekly, monthly),
        (hourly_nm, daily_nm, weekly_nm, monthly_nm),
        data,
        data_nm
    )

