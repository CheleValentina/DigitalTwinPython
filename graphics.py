import re

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb


# ToDo before calling this function check the frequency of plotting the user wants - e.g hourly
# ToDo before calling this function check the feature the user wants - e.g Active_Power, Loss
# date type 2022-06-07
def plot_data_between_date_interval(data, initial_date, last_date, feature, filename):
    data[initial_date:last_date][feature].plot(figsize=(15, 7))
    plt.savefig(filename, bbox_inches="tight", pad_inches=0.25, dpi=500)
    plt.clf()


def plot_data_information(data, filename):
    plt.clf()
    plt.axis("off")
    plt.table(
        cellText=data.head().values.round(2),
        colLabels=data.head().columns,
        loc="center",
    )
    plt.savefig(filename, bbox_inches="tight", pad_inches=0.25, dpi=500)
    plt.clf()


def plot_data_statistics(data, filename):
    plt.axis("off")
    plt.table(
        cellText=data.describe().values.round(2),
        colLabels=data.describe().columns,
        loc="center",
        rowLabels=data.describe().index,
    )
    plt.savefig(filename, bbox_inches="tight", pad_inches=0.25, dpi=500)
    plt.clf()


def plot_speed_power_relation(data, folder_name):
    sb.histplot(data=data, y="Active_Power", x="Wind_Speed")
    plt.savefig(folder_name + "/speed_power_relation.png", transparent=True)
    plt.clf()

    sb.histplot(data=data, y="Theoretical_Power", x="Wind_Speed")
    plt.savefig(folder_name + "/speed_theoretical_power_relation.png", transparent=True)
    plt.clf()


def plot_data_distribution(data, folder_name):
    for feature in data.columns:
        sb.histplot(data=data, x=feature, fill=False, element="step")
        plt.savefig(
            folder_name + "/" + re.sub(r"\(.*\)", "", feature) + "_distribution.png",
            bbox_inches="tight",
            pad_inches=0.25,
            dpi=500,
            transparent=True,
        )
        plt.clf()


def plot_power_by_date(data, filename):
    data["Active_Power"].interpolate().plot(figsize=(20, 5))

    plt.savefig(filename)
    plt.clf()


def plot_loss(data, filename):
    data["Loss"].interpolate().plot()

    plt.savefig(filename)
    plt.clf()


def plot_power_daily_monthly(monthly, weekly, filename):
    monthly["Active_Power"].interpolate().plot(label="monthly")
    weekly["Active_Power"].interpolate().plot(label="weekly")
    plt.title("Daily and Monthly Average Power Generated")
    plt.ylabel("LV Power (kW)")
    plt.xlabel("Date")
    plt.legend()
    plt.savefig(filename)
    plt.clf()
