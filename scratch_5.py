#D:\data
import pandas
import xlwt
#df = pandas.read_csv('D:\data\TT and LATlong.csv')
df1 = pandas.read_excel('D:\data\TT and LATlong1.xls')

a=(df1.unique_ID)
b=pandas.to_numeric(a)
#print(df1.dtypes)
print('len(df1[unique_ID])')
print(len(df1['unique_ID']))


unique_values=a.unique()
print('len(unique_values)')
print(len(unique_values))
#id=pandas.DataFrame(columns=['num','freq'])
#print((id.count))
id=(df1.groupby('unique_ID').unique_ID.count())
#print(id)
#print(type(id))
id.to_excel('D:\id.xls')
li=pandas.read_excel('D:\id.xls')
#print(li.columns)
l=[43468100819,43468747413,4346820210261]
#l=[4346820210261]
df3=pandas.DataFrame(columns=['unique_ID','first_latitude','last_latitude','first_longitude','first_time','last_time'])
df4=df3
for i in unique_values:
   c= li.loc[li['unique_ID']==i]
   count=c['unique_ID.1']
   print('count='+str(count))

   ind = df1.index[df1['unique_ID'] == i]
   print("index-"+str((ind[0])))
   print(ind)
   first = df1.iloc[ind[0]]
   print("first")
   #print(first)
   #print("length="+str(len(r)))
   #first = r.iloc[[0]]
   t_first_latitude, t_first_longitude, t_first_time = first['latitude'], first['longitude'], first['time']
   #ind = (ind + count - 1)
   print('t_first_latitude')
   print(t_first_latitude)
   df2 = df1.iloc[ind[-1]]
   print('df2')
   print(df2)
   t_last_latitude, t_last_longitude, t_last_time = df2['latitude'], df2['longitude'], df2['time']
   print('t_last_latitude')
   print(t_last_latitude)

   df3['unique_ID']=[i]
   df3['first_latitude']=[t_first_latitude]
   df3['last_latitude']=[t_last_latitude]
   df3['first_longitude'] =[ t_first_longitude]
   df3['last_longitude'] = [t_last_longitude]
   df3['first_time']=[t_first_time]
   df3['last_time']=[t_last_time]

   print(str(len(df3))+'df3')
   df4=df4.append(df3,ignore_index=True)
print(df4)
df4.to_excel("D:\df4.xls")

print(len(df4))
   # li.loc[df1['unique_ID']==i]


