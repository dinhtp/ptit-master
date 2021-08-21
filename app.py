import time
from analytic import source, analyze
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

start_time = time.time()
X, Y = source.list_data()

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=analyze.TEST_SIZE,
    random_state=analyze.RANDOM_STATE
)

model = RandomForestClassifier(
    n_estimators=analyze.NO_ESTIMATORS,
    random_state=analyze.RANDOM_STATE
)

model.fit(X_train, Y_train)

predict_data = X_test
#predict_data = source.find_one('25', len(X_test))
prediction = model.predict(predict_data)
accuracy = metrics.accuracy_score(Y_test, prediction)
features = source.get_feature_importance(
    model.feature_importances_,
    list(X.columns)
)


print("Test Size: %.2f" % analyze.TEST_SIZE)
print("No of Estimates: %d" % analyze.NO_ESTIMATORS)
print("Random State: %d" % analyze.RANDOM_STATE)

print("")
print("Accuracy: %.4f %%" % accuracy)
print("Important Features:")
print(features * 100)

print("")
print("--- Executed in: %s seconds ---" % (time.time() - start_time))
