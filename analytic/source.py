import pandas as pd
from database import engine, connector


def update_prediction(session_id, prediction):
    connection, cursor = connector.connect()
    cursor.execute(
        "UPDATE master_sale_session SET prediction = %s WHERE id = %s",
        (prediction, session_id)
    )
    connection.commit()
    connector.disconnect(connection=connection, cursor=cursor)


def find_one(id, loop_times):
    new_engine = engine.open_engine()
    session = pd.read_sql(build_query(id), new_engine)
    engine.close_engine(mysql_engine=new_engine)

    list_data = []
    session_data = session.drop(['is_checkout_cart'], 1)
    for _ in range(loop_times):
        list_data.append(session_data)

    return pd.concat(list_data)


def list_data():
    new_engine = engine.open_engine()
    data = pd.read_sql(build_query(session_id=''), new_engine)
    engine.close_engine(mysql_engine=new_engine)

    train_data = data.drop(['is_checkout_cart'], 1)
    test_data = data['is_checkout_cart'].values
    test_data = test_data.astype("int")

    return train_data, test_data


def get_feature_importance(features, columns):
    return pd.Series(features, columns).sort_values(ascending=False)


def build_query(session_id):
    sql = "SELECT device_type, origin, CAST(average_interval AS INT) AS average_interval,"
    sql += "total_view, total_product_view, total_cart_view,"
    sql += "total_category_view, total_search, total_item_qty, CAST(total_cart_value AS INT) AS total_cart_value,"
    sql += "is_checkout_cart FROM master_sale_session "

    if session_id == None or session_id == '':
        sql += "LIMIT 536"
    else:
        sql += "WHERE id = %d" % int(session_id)

    return sql
