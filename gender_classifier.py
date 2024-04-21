from sklearn import tree

clf = tree.DecisionTreeClassifier()
# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


clf = clf.fit(X, Y)
h = int(input('Enter your height in cm: '))
w = int(input('Enter your weight in kg: '))
s = int(input('Enter your shoe size in cm: '))
prediction = clf.predict([[h, w, s]])



print('You are a ',prediction[0])
