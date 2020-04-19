# coding: utf-8

import pandas as pd
import itertools, datetime
import matplotlib.pyplot as plt

def ISOdate(date):
    return pd.Timestamp(date).strftime('%Y-%m-%d')
    
def cleanup_frame(df):
    df.columns=itertools.chain(map(str.lower,df.columns[:4]),map(ISOdate,df.columns[4:]))
    return df.rename(columns={'province/state':'state','country/region':'country'}).groupby('country').sum().drop(columns=['lat','long'])

def cleanup_frame_US(kind,df):
    date_start_column=11
    drop_columns=['uid', 'iso2', 'iso3', 'code3', 'fips', 'admin2','lat','long','combined_key']
    if kind == 'deaths':
        date_start_column+=1
        drop_columns.append('population')
    df.columns=itertools.chain(map(str.lower,df.columns[:date_start_column]),map(ISOdate,df.columns[date_start_column:]))
    return df.rename(columns={'province_state':'state','country_region':'country','long_':'long'}).drop(columns=drop_columns).groupby('state').sum()

def get_data(kind='confirmed',US_states=False):
    if not US_states:
        if kind in ('confirmed','deaths','recovered'):
            return cleanup_frame(pd.read_csv(f'csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_{kind}_global.csv'))
        elif kind == 'infected':
            return get_data('confirmed',US_states).sub(get_data('recovered'),US_states).add(get_data('deaths',US_states))
        else:
            raise TypeError(f'Unknown kind: {kind}')
    else:
        if kind in ('confirmed','deaths'):
            return cleanup_frame_US(kind,pd.read_csv(f'csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_{kind}_US.csv'))
        elif kind == 'infected':
            return get_data('confirmed',US_states).sub(get_data('deaths',US_states))
            
def calculate_nd_mean(df,n=14):
    return df.rolling(window=n,axis='columns',min_periods=1).mean()

def chart(df,countries,title="No title",file=None):
    plt.figure()
    plt.suptitle(title)
    if isinstance(countries,list):
        for country in countries:
            df.loc[country].plot()
        plt.legend(loc='upper left')
    else:
        df.loc[countries].plot()
    if file:
        plt.savefig(file)
    else:
        plt.show()

def order_with_latest_data(df):
    yesterday=datetime.date.today()-datetime.timedelta(days=1)
    return df.sort_values(by=yesterday.isoformat(),axis='index',ascending=False,inplace=False)

def topchart(kind,count=10,file=None,US_states=False, mean=False):
    title=kind
    if US_states:
        title += " in US states"
    else:
        title += " globally"
    if mean:
        title += " (14 day average)"
        df=order_with_latest_data(calculate_nd_mean(get_data(kind,US_states)))
    else:
        df=order_with_latest_data(get_data(kind,US_states))
    chart(df,list(df.head(count).index),title=title,file=file)

def create_topchart_files(directory=None):
    nameparts={}
    filenametemplate="{directory}/{kind}{place}{mean}.png"
    nameparts['directory']=directory if directory else "."
    for mean in (False,True):
        nameparts['mean']="_c14davg" if directory else ""
        nameparts['place']=""
        for kind in ('confirmed','recovered','deaths','infected'):
            nameparts['kind']=kind
            topchart(kind,file=filenametemplate.format(**nameparts), mean=mean)
        nameparts['place']="_US"
        for kind in ('confirmed','deaths','infected'):
            nameparts['kind']=kind
            topchart(kind,file=filenametemplate.format(**nameparts),US_states=True,mean=mean)

if __name__ == '__main__':
    create_topchart_files()
