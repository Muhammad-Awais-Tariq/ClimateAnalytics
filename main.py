import numpy as np
import pandas as pd

cities_name = {"Kamra" : 0 , "Islamabad" : 1 , "Karachi" : 2 , "Kohat" : 3}
months = {0 : "Jan" , 1 : "Feb" , 2 : "Mar" ,  3: "Apr" , 4 : "May" , 5: "Jun" , 6: "Jul" , 7: "Aug"  , 8: "Sep" , 9: "Oct" , 10: "Nov" , 11 : "Dec"}
cities_idx = {0 :"Kamra" , 1: "Islamabad" , 2 :"Karachi"  ,3 : "Kohat"}

def get_data():
    """
    This function generates the data of 4 cities randomly and then returns that in the form of the numpy array
    """
    
    #using numpy
    final2 = np.random.randint(low=(20,40,0) , high=(45,90,300) , size=(4,12,3)) #  4 ctities 12 moths and 3 readings temp , humidity , rainfall 

    return final2

def get_csv(location):
    weater_df = pd.read_csv(location)
    return weater_df

def avg(data):
    required_data = data [:,:,0]
    avg = np.round(np.mean(required_data  , 1) , 2)     
    avg_all =  np.round(np.mean(avg) ,2)

    return avg , avg_all

def max_rain(data):
    required_Data = data [:,:,1]
    max_rainfall = np.max(required_Data ,1)
    index = np.argmax(required_Data ,1 )
    return max_rainfall , index

def min_humidity(data):
    required_Data = data [:,:,2]
    minimum_humidity = np.min(required_Data ,1)
    index = np.argmin(required_Data , 1)
    return  minimum_humidity  , index

def std_temp(data):
    required_Data = data [:,:,0]
    standard_temp = np.std(required_Data ,1)
    return  standard_temp

def compare_months_rainfall(data):
    first_6_months = data[:,0:6, 2]
    last_6_months = data[:,6:,2]
    if first_6_months.sum() > last_6_months.sum():
        return "Summer has more rainfall"
    elif last_6_months.sum() > first_6_months.sum():
        return "winter has more rainfall"
    else:
        return "Both summer and winter has equal amount of rain"

def compare_temp(data , city1 , city2):
    city1_avg = np.round(np.average(data[cities_name[city1] , : , 0]) ,2 )
    city2_avg = np.round(np.average(data[cities_name[city2] , : , 0]) ,2 )
    
    if city1_avg > city2_avg:
        return f"{city1} is hotter"
    elif city2_avg > city1_avg:
        return f"{city2} is hotter"

def hottest_month(data):
    average = np.average(data[:,:,0],0)
    maximum_temp = np.max(average)
    maximum_temp_idx = np.argmax(average)
    print(f"The hottest month is {months[maximum_temp_idx]} with an average temp of {maximum_temp}")

def coldest_month(data):
    average = np.average(data[:,:,0],0)
    minimum_temp = np.min(average)
    minimum_temp_idx = np.argmin(average)
    print(f"The coldest month is {months[minimum_temp_idx]} with an average temp of {minimum_temp}")  

def unusual_rainfall(data):
    rainfall = data[:, :, 2]

    average = np.mean(rainfall, axis=0)
    std_rainfall = np.std(rainfall, axis=0)
    threshold = average + 2 * std_rainfall

    flags = rainfall > threshold
    indexes = np.where(flags)

    for city_idx, month_idx in zip(indexes[0], indexes[1]):
        city_idx = int(city_idx)  
        month_idx = int(month_idx)
        print(
            f"{cities_idx[city_idx]} - {months[month_idx]} - "
            f"{rainfall[city_idx, month_idx]} (UNUSUAL)"
        )

def get_city_data(df , city):
    city_df = df[df.City == city]
    print(city_df)

def get_weather_partition(df , weather): # 0 for summer 1 for winter
    if weather == 0:
        new_df = df[(df.Month == "Jan") | (df.Month == "Feb") | (df.Month == "Mar") | (df.Month == "Apr") | (df.Month == "May") | (df.Month == "Jun")  ]
    elif weather == 1:
        new_df = df[(df.Month == "Jul") | (df.Month == "Aug") | (df.Month == "Sep") | (df.Month == "Oct") | (df.Month == "Nov") | (df.Month == "Dec")  ]
    city_df = new_df.groupby("City")[["Temperature" , "Humidity" , "Rainfall"]].mean()
    print(city_df)

def get_rain_above_threshold(df , amount):
    rain_df = df[df.Rainfall > amount][["City" , "Month" , "Rainfall"]]
    print(rain_df)

def main():
    weather_df = get_csv("climate_data(1).csv")
    # print(weather_df.info())
    # print(weather_df.describe())
    # print(weather_df.columns)
    # print(weather_df.shape)
    # print(weather_df.head())
    # get_city_data(weather_df , "Kamra")
    # get_weather_partition(weather_df , 1)
    get_rain_above_threshold(weather_df , 100)

if __name__ == "__main__":
    main()
