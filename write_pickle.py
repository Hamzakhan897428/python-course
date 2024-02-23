import pickle
i=[1,2,3,4,5,6,7]
file_path='writedata.txt'
with open(file_path,'wb')as file:
    pickle.dump(i,file)
print("data has been save as",file_path)