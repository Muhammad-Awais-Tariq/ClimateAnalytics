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



if __name__ == "__main__":
    main()
