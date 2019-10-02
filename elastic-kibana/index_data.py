# !/bin/python
# pip install elasticsearch
from elasticsearch import Elasticsearch
import pandas as pd
import json
import uuid

ES_ENDPOINT = 'http://35.247.73.246:9200'
DATA_INDEX = 'claims'
DATA_FILE= '/Users/dsharris/Projects/cfc-workspace/Raw data/lajc_clean.csv'

es = Elasticsearch([ES_ENDPOINT])

if __name__ == '__main__':
  claims_df = pd.read_csv(DATA_FILE)
  docs = json.loads(claims_df.to_json(orient='records'))
  for doc in docs:
    doc_id = str(uuid.uuid4())
    es.index(index=DATA_INDEX, doc_type='_doc', id=doc_id, body=json.dumps(doc))


