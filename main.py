import numpy as np

cities = {"Kamra" : 0 , "Islamabad" : 1 , "Karachi" : 2 , "Kohat" : 3}
months = {0 : "Jan" , 1 : "Feb" , 2 : "Mar" ,  3: "Apr" , 4 : "May" , 5: "Jun" , 6: "Jul" , 7: "Aug"  , 8: "Sep" , 9: "Oct" , 10: "Nov" , 11 : "Dec"}

def get_data():
    """
    This function generates the data of 4 cities randomly and then returns that in the form of the numpy array
    """
    

    #using numpy
    final2 = np.random.randint(low=(20,40,0) , high=(45,90,300) , size=(4,12,3)) #  4 ctities 12 moths and 3 readings temp , humidity , rainfall 

    return final2

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
    city1_avg = np.round(np.average(data[cities[city1] , : , 0]) ,2 )
    city2_avg = np.round(np.average(data[cities[city2] , : , 0]) ,2 )
    
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

def main():
    complete_data = get_data()
    coldest_month(complete_data)

if __name__ == "__main__":
    main()
