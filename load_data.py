import pickle
file=open('writedata.txt','rb')
i=pickle.load(file)
print(i)