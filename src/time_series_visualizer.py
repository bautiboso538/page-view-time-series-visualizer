import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def clean_data(df):
    # Filtrar el 2.5% superior e inferior
    low = df['value'].quantile(0.025)
    high = df['value'].quantile(0.975)
    return df[(df['value'] >= low) & (df['value'] <= high)]

def draw_line_plot(df):
    df = clean_data(df.copy())
    plt.figure(figsize=(15, 5))
    plt.plot(df.index, df['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

def draw_bar_plot(df):
    df = clean_data(df.copy())
    df['year'] = df.index.year
    df['month'] = df.index.month
    # Agrupar y pivotear para meses en orden
    bar_data = df.groupby(['year', 'month'])['value'].mean().unstack()
    # Nombres de meses abreviados
    bar_data.columns = [pd.to_datetime(str(m), format='%m').strftime('%b') for m in bar_data.columns]
    bar_data.plot(kind='bar', figsize=(12, 6))
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()

def draw_box_plot(df):
    df = clean_data(df.copy())
    df['year'] = df.index.year
    df['month'] = df.index.strftime('%b')
    df['month_num'] = df.index.month
    # Ordenar meses correctamente
    df = df.sort_values('month_num')
    plt.figure(figsize=(15, 6))
    # Year-wise
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    # Month-wise
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df, order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.tight_layout()
    plt.savefig('box_plot.png')
    plt.show()