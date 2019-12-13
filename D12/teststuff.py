with open("input.txt","r") as f: data=f.readlines()
# with open("test.txt","r") as f: data=f.readlines()
dataNew=[]
dataNew = [("").join(list(filter(lambda ch: ch not in "<>xyz= ", x))[:-1]).split(",") for x in data]
print(dataNew)