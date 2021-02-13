import pandas as pd

wage_data = pd.read_csv('wage.csv', header=None)
wage_predictors = wage_data.iloc[:, 0:-1].to_numpy()
wage_target = wage_data.iloc[:, -1].to_numpy()


def _pre_process_titanic(data_frame, age_fill):
    result = data_frame.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])

    titanic_df_age_missing = data_frame[['Age']].isna().astype(int)
    titanic_df_age_missing.columns = ['age_was_missing']
    titanic_df_sex = pd.get_dummies(result['Sex'], drop_first=True)
    titanic_df_embarked = pd.get_dummies(result['Embarked'], drop_first=False, prefix='Embarked')

    result.drop(columns=['Sex', 'Embarked'], inplace=True)
    result = result.join([titanic_df_age_missing, titanic_df_sex, titanic_df_embarked])
    result.rename(str.lower, axis='columns', inplace=True)
    result['age'] = result['age'].fillna(value=age_fill)
    return result


titanic_train = pd.read_csv('titanic_train.csv')
titanic_train_df = _pre_process_titanic(titanic_train, titanic_train['Age'].mean())

titanic_train_predictors = titanic_train_df.drop(columns=['survived']).to_numpy()
titanic_train_target = pd.get_dummies(titanic_train_df['survived']).to_numpy()

titanic_test = pd.read_csv('titanic_test.csv')
titanic_test_df = _pre_process_titanic(titanic_test, titanic_train['Age'].mean())
titanic_test_predictors = titanic_test_df.to_numpy()

print(titanic_test_df.describe())
