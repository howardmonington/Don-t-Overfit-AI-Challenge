import pandas as pd
import numpy as np
pd.set_option('max_rows', None)
pd.set_option('max_columns',None)
import xgboost as xgb

train = pd.read_csv(r'C:\Users\lukem\Desktop\Github AI Projects\Data for ai competitions\don-t overfit II\train.csv')
test = pd.read_csv(r'C:\Users\lukem\Desktop\Github AI Projects\Data for ai competitions\don-t overfit II\test.csv')
sample_submission = pd.read_csv(r'C:\Users\lukem\Desktop\Github AI Projects\Data for ai competitions\don-t overfit II\sample_submission.csv')

y = train.target
train = train.drop('target', axis = 1)

clf = xgb.XGBClassifier(
    n_estimators=50,
    max_depth=3,
    learning_rate=0.05,
    subsample=0.9,
    colsample_bytree=0.9,
    random_state=2019,
    tree_method='gpu_hist'  # THE MAGICAL PARAMETER
)

clf.fit(train, y)

pred = pd.DataFrame(clf.predict(test), dtype='int64')
submission = pd.DataFrame(test['id'])
submission['target'] = pred


path = r'C:\Users\lukem\Desktop\Github AI Projects\Submissions\don-t overfit ii ai challenge\ '
submission.to_csv(path + 'master_branch_v1.csv', index=False)

