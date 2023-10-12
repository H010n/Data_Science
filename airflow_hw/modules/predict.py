# <YOUR_IMPORTS>
import pandas as pd
import dill
import json
import glob
import os


def predict():
    # <YOUR_CODE>
    path = os.path.expanduser('~/airflow_hw')
    with open(f'{path}/data/models/cars_pipe_202310102022.pkl', 'rb') as file:
        model = dill.load(file)
    df_pred = pd.DataFrame(columns=['car_id', 'pred'])
    print('ok')
    path_files = path + '/data/test/*json'
    for json_files_path in glob.iglob(path_files):
        with open(json_files_path) as fin:
            form = json.load(fin)
            print(form)
            df = pd.DataFrame.from_dict([form])
            print(df)
            pred = model.predict(df)


if __name__ == '__main__':
    predict()