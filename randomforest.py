from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import dataset_X
import dataset_Y

x_train = [
    dataset_X
]
y_train = [dataset_Y]

parameter_grid = {
            'criterion': ['entropy', 'gini'],
            'max_depth': [10, 20, 100],
            'n_estimators': [10, 20, 100]
        }
clf = RandomForestClassifier()
grid_searcher = GridSearchCV(clf, parameter_grid, verbose=2)
grid_searcher.fit(x_train, y_train)
clf_best = grid_searcher.best_estimator_
 
print('Best params = ', clf_best.get_params())

 
scores = cross_val_score(clf_rf, x_train, y_train, cv=10)
print(scores)