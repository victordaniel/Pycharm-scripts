#D:\data
import pandas
#df = pandas.read_csv('D:\data\TT and LATlong.csv')
df1 = pandas.read_excel('D:\data\TT and LATlong1.xls')
#print(df)
#print(df.columns)
a=(df1.unique_ID)
#print((a))

unique_values=a.unique()
print(len(unique_values))
print(df1.groupby('unique_ID').unique_ID.count())
df2=pandas.DataFrame(columns=['unique_ID','first_latitude','last_latitude','first_longitude','last_longitude','first_time','last_time'])
#print(type(df2))
k=0
print(df1.columns)
t_unique_ID=0
for i in df1.index:
    id=df1.unique_ID[i]
    #print(id)
    if(id != t_unique_ID):
        t_unique_ID,t_first_latitude,t_first_longitude,t_first_time=df1.unique_ID,df1.latitude,df1.longitude,df1.time
        t_last_latitude, t_last_longitude,t_last_time = df1.latitude, df1.longitude, df1.time
    elif(df1.unique_ID==t_unique_IDid):
        t_last_latitude,t_last_longitude,t_last_time=df1.latitude,df1.longitude,df1.time
    df2.unique_ID[i],df2.first_latitude,df2.last_latitude,df2.first_longitude,df2.last_longitude,df2.first_time,df2.last_time=t_unique_ID,t_first_latitude,t_last_latitude,t_first_longitude,t_last_longitude,t_first_time,t_last_time
print(df2)
df2.to_excel("df2.xlsx")


