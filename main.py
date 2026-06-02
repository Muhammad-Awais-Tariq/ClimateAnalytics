import numpy as np

def main():
    cities = ["Kamra" , "Islamabad" , "Karachi" , "Kohat"]
    months = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug"  , "Sep" , "Oct" , "Nov" , "Dec"]
    final = []
    for city in cities:
        for month in months:
            temp = np.random.randint(20, 45)
            humidity = np.random.randint(40, 90)
            rainfall = np.random.randint(0, 300)

            final.append([city , month , temp , humidity , rainfall])

    print(final)

    #using numpy
    final2 = np.random.randint(low=(20,40,0) , high=(45,90,300) , size=(4,12,3))  # 4 ctities 12 moths and 3 readings
    print(final2)
    print(final2[0][0]) #kamra janaury temparatur

if __name__ == "__main__":
    main()
