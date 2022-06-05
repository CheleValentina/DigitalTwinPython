import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import re

data = pd.read_csv("datasets/wind-turbine-scada-dataset/T1.csv").rename(
    columns={"Date/Time": "Date",
             "LV ActivePower (kW)": "Active_Power(kW)",
             "Wind Speed (m/s)": "Wind_Speed(m/s)",
             "Theoretical_Power_Curve (KWh)": "Theoretical_Power(kWh)",
             "Wind Direction (°)": "Wind_Direction"
             }
).round(2)


def plot_data_information():
    plt.axis('off')
    plt.table(cellText=data.head().values, colLabels=data.head().columns, loc='center')
    plt.savefig('plots/sample_of_data.png', bbox_inches='tight', pad_inches=0.25, dpi=500)
    plt.clf()


def plot_data_statistics():
    plt.axis('off')
    plt.table(cellText=data.describe().values.round(2), colLabels=data.describe().columns,
              loc='center', rowLabels=data.describe().index)
    plt.savefig('plots/describe_data.png', bbox_inches='tight', pad_inches=0.25, dpi=500)
    plt.clf()


def plot_speed_power_relation():
    sb.histplot(data=data, y='Active_Power(kW)', x='Wind_Speed(m/s)')
    plt.savefig('plots/speed_power_relation.png', transparent=True)
    plt.clf()

    sb.histplot(data=data, y='Theoretical_Power(kWh)', x='Wind_Speed(m/s)')
    plt.savefig('plots/speed_theoretical_power_relation.png', transparent=True)
    plt.clf()


def plot_data_distribution():
    for feature in data.columns:
        if feature != "Date":
            sb.histplot(data=data, x=feature, fill=False, element='step')
            plt.savefig('plots/' + re.sub(r"\(.*\)", "", feature) + '_distribution.png', bbox_inches='tight',
                        pad_inches=0.25, dpi=500, transparent=True)
            plt.clf()


if __name__ == '__main__':
    plot_data_information()
    plot_data_statistics()
    # plot_speed_power_relation()
    # plot_data_distribution()
