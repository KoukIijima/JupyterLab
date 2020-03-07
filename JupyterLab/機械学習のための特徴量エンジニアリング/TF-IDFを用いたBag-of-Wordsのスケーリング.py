import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer

# review dataを読み込む
with open('yelp_academic_dataset_review.json') as f:
    js = []
    for i in range(10000):
        js.append(json.loads(f.readline()))

# DataFrameに変換
review_df = pd.DataFrame(js)

# お店のデータセットを読み込む
with open('yelp_academic_dataset_business.json') as biz_f:
    biz_df = pd.DataFrame([json.loads(x) for x in biz_f.readlines()])

'''
お店がNightlifeの場合がTrue
Resturantの場合はFalseと場合分けをする
'''
index = []
target = []
for j, value in enumerate(biz_df['categories']):
    if (value):
        a = set(value.split(', '))
    if (len(a & set(['Nightlife'])) > 0):
        index.append(j)
        target.append(True)
    elif (len(a & set(['Restaurants'])) > 0):
        index.append(j)
        target.append(False)

twobiz = pd.DataFrame({'Target':target},index = index)

twobiz_review = pd.concat([biz_df, twobiz], axis = 1, join = 'inner')

cleaned_twobiz_review = twobiz_review.merge(review_df, on='business_id', how='inner')

# 必要な特徴量のみを残す
cleaned_twobiz_review = cleaned_twobiz_review[['business_id', 'name', 'stars_y', 'text', 'categories', 'Target']]
