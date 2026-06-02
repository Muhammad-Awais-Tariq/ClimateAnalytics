import numpy as np

def get_data():
    """
    This function generates the data of 4 cities randomly and then returns that in the form of the numpy array
    """
    cities = ["Kamra" , "Islamabad" , "Karachi" , "Kohat"]
    months = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug"  , "Sep" , "Oct" , "Nov" , "Dec"]

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
    index = np.argmax(max_rainfall)
    return max_rainfall , index

def main():
    complete_data = get_data()

if __name__ == "__main__":
    main()
