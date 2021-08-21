from analytic import source
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics


TEST_SIZE = 0.1
RANDOM_STATE = 10
NO_ESTIMATORS = 10


def analyze(session_id):
    session_data = source.find_one(session_id)
    train_data, test_data = source.list_data()

    x_train, x_test, y_train, y_test = train_test_split(
        train_data,
        test_data,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )
    model = RandomForestClassifier(
        n_estimators=NO_ESTIMATORS,
        random_state=RANDOM_STATE
    )
    model.fit(x_train, y_train)

    prediction = model.predict(x_test)
    accuracy = metrics.accuracy_score(y_test, prediction)
    features = source.get_feature_importance(
        model.feature_importances_,
        list(train_data.columns)
    )

    print(session_data)

    return accuracy, features
