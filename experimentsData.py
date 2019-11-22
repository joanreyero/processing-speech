import pandas as pd

def experiment_1(df, name, n_train, n_test):
    females = df['Gender'] == 'f'
    males = df['Gender'] == 'm'
    save_names(make_samples(df[females], n_train, df[males], n_test),
               name)

def make_samples(df_train, n_train, df_test, n_test):
        train_sample = df_train.sample(n=n_train)
        df_test = remove_sample(df_test, train_sample)
        test_sample = df_test.sample(n=n_test)
        return [train_sample, test_sample]              


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
    t = ['train', 'test']
    for n in range(2):
        dfs[n]['Name'].to_csv(experiment + '_' + t[n] + '.txt',
                              header=False, index=False)


def main():
    df = pd.read_csv('log.csv')
    experiment_1(df, 'try', 50, 20)

if __name__ == "__main__":
    main()
