from sklearn import tree
#first index is how many people it seats and the second is weight of car
features = [[5,2979],[5,3497],[5,4336],[3,3470],[3,3689],[7,4259],[7,6547]]
labels = [0,0,0,1,1,1,1] #0 = car  1 = truck 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
while True:
	print(" Car type Predicter \n")
	x = input("enter number of people car can hold\n")
	y = input("Enter weight \n")
	result = (clf.predict([[x,y]]))
	if (result == 1):
		print("\nTruck")
	elif (result == 0):
		print("\nCar")
		
