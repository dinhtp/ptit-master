from analytic import source
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


TEST_SIZE = 0.1
RANDOM_STATE = 10
NO_ESTIMATORS = 10


def predict(session_id):
    train_data, test_data = source.list_data()
    x_train, x_test, y_train, _ = train_test_split(
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
    session_data = source.find_one(session_id, len(x_test))
    prediction = model.predict(session_data)

    source.update_prediction(int(session_id), int(prediction[0]))
