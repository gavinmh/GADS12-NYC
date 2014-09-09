"""


"""
import numpy as np
import mahotas as mh
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from os import walk
from sklearn.preprocessing import scale
import os

X = []
y = []
for dirpath, dirnames, filenames in walk('data/att-faces/orl_faces'):
    for fn in filenames:
        if fn[-3:] == 'pgm':
            image_filename = os.path.join(dirpath, fn)
            X.append(scale(mh.imread(image_filename, as_grey=True).reshape(10304).astype('float32')))
            y.append(dirpath)

X = np.array(X)
X_train, X_test, y_train, y_test = train_test_split(X, y)

n_components = 150
print 'Reducing the dimensions...'
pca = PCA(n_components=n_components)
X_train_reduced = pca.fit_transform(X_train)
X_test_reduced = pca.transform(X_test)
print X_train_reduced.shape
print X_test_reduced.shape

print 'Training the classifier...'
classifier = LogisticRegression()
classifier.fit_transform(X_train_reduced, y_train)
print classifier.score(X_test_reduced, y_test)
predictions = classifier.predict(X_test_reduced)
print classification_report(y_test, predictions)

for i, p in enumerate(predictions):
    print p, y_test[i]

print 'Training the classifier on the unreduced data...'
classifier = LogisticRegression()
classifier.fit_transform(X_train, y_train)
print classifier.score(X_test, y_test)
predictions = classifier.predict(X_test)
print classification_report(y_test, predictions)
