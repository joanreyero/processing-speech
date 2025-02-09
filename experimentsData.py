import pandas as pd

def gender_headset(df, name, n_train, n_test):
    females = df.loc[(df['Gender'] == 'f') & (df['Microphone'].isin(['headset', 'logitech_headset']))]
    males = df.loc[(df['Gender'] == 'f') & (df['Microphone'].isin(['headset', 'logitech_headset']))]
    save_names(make_samples(females, n_train, males, females, n_test),
               name)


def gender(df, name, n_train, n_test):
    females = df.loc[(df['Gender'] == 'f')]
    males = df.loc[(df['Gender'] == 'f')]
    save_names(make_samples(females, n_train, males, females, n_test),
               name)

def microphone_simple(df, name, n_train, n_test):
    phone = df.loc[df['Microphone'].str.contains("Samsung|iphone|iPhone|oneplus|samsung|HUAWEI")==True]
    computer = df.loc[df['Microphone'] == 'iMac']
    headset = df.loc[df['Microphone'].isin(['headset', 'logitech_headset'])]
    save_names(make_samples(headset, n_train, computer, phone, n_test),
               name)

def microphone_double(df, name, n_train, n_test):
    computer = df['Microphone'] == 'iMac'
    headset = df['Microphone'].isin(['headset', 'logitech_headset'])
    computer_headset = df.loc[computer | headset]
    phone = df.loc[df['Microphone'].str.contains("Samsung|iphone|iPhone|oneplus|samsung|HUAWEI")==True]
    save_names(make_samples(computer_headset, n_train, computer_headset, phone, n_test),
               name)


def accent_n_to_nn(df, name, n_train, n_test):
    native = df.loc[df['Accent'].str.contains("NA")==True]
    non_native = df.loc[df['Accent'].str.contains("NN")==True]
    save_names(make_samples(native, n_train, non_native, native, n_test),
               name)

def accent_nn_to_n(df, name, n_train, n_test):
    native = df.loc[df['Accent'].str.contains("NA")==True]
    non_native = df.loc[df['Accent'].str.contains("NN")==True]
    save_names(make_samples(non_native, n_train, non_native, native, n_test),
               name)

def general(df, name, n_train, n_test):
       save_names(make_samples(df, n_train, df, df, n_test),
               name)


def make_samples(df_train, n_train, df_test, df_test_2, n_test):
        train_sample = df_train.sample(n=n_train)
        df_test = remove_sample(df_test, train_sample)
        test_sample = df_test.sample(n=n_test)
        df_test_2 = remove_sample(df_test_2, test_sample)
        df_test_2 = remove_sample(df_test_2, train_sample)
        test_sample_2 = df_test_2.sample(n=n_test)
        return [train_sample, test_sample, test_sample_2]


def remove_sample(df, sample):
    """ Remove all rows that are in sample and in df.
    """
    return (pd.merge(df,sample, indicator=True, how='outer')
            .query('_merge=="left_only"')
            .drop('_merge', axis=1))


def save_names(dfs, experiment):
    """ Saving the names of the training and testing dataframes.
    - Input: an array [Train DF, Test DF]
    """
    t = ['train', 'test', 'test-2']
    for n in range(3):
        dfs[n]['Name'].to_csv('experiment-data/' + experiment + '-' + t[n] + '.txt',
                              header=False, index=False)


def sanity_check(df, good_users_file):
    users_file = open(good_users_file, 'r')
    users = [line[:-1] for line in users_file.readlines()]
    return df[df['Name'].isin(users)]

def main():
    df = pd.read_csv('log.csv')
    df = sanity_check(df, 'sanity_users.txt')
    gender_headset(df, '1-gender-headset', 20, 10)
    gender(df, '2-gender', 20, 10)
    microphone_simple(df, '3-microphone-simple', 20, 10)
    microphone_double(df, '4-microphone-double', 20, 10)
    accent_n_to_nn(df, '5-accent-native-nn', 20, 10)
    accent_nn_to_n(df, '6-accent-nn-native', 20, 10)
    general(df, '7-sample-50', 50, 10)
    general(df, '8-sample-20', 20, 10)


if __name__ == "__main__":
    main()
