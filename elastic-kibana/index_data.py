# !/bin/python
# pip install elasticsearch
from elasticsearch import Elasticsearch
import pandas as pd
import json
import uuid

ES_ENDPOINT = 'https://search-lajc-wage-theft-oiaka2yn2mw4onwkkslm4oy4pa.us-east-1.es.amazonaws.com/'
DATA_INDEX = 'claims'
DATA_FILE= '../Raw data/lajc_clean.csv'

es = Elasticsearch([ES_ENDPOINT])

if __name__ == '__main__':
  claims_df = pd.read_csv(DATA_FILE)
  docs = json.loads(claims_df.to_json(orient='records'))
  for doc in docs:
    doc_id = str(uuid.uuid4())
    es.index(index=DATA_INDEX, doc_type='_doc', id=doc_id, body=json.dumps(doc))

# https://search-lajc-wage-theft-oiaka2yn2mw4onwkkslm4oy4pa.us-east-1.es.amazonaws.com/_plugin/kibana/app/kibana#/dashboard/08157150-e578-11e9-8e9b-cf6e52d7d1e7?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-4y,to:now))&_a=(description:'',filters:!(),fullScreenMode:!f,options:(hidePanelTitles:!f,useMargins:!t),panels:!((embeddableConfig:(),gridData:(h:15,i:'1',w:24,x:0,y:0),id:'6e03a350-e574-11e9-8e9b-cf6e52d7d1e7',panelIndex:'1',type:visualization,version:'7.1.1'),(embeddableConfig:(),gridData:(h:15,i:'2',w:24,x:24,y:0),id:'3b55a140-e576-11e9-8e9b-cf6e52d7d1e7',panelIndex:'2',type:visualization,version:'7.1.1'),(embeddableConfig:(),gridData:(h:15,i:'3',w:24,x:0,y:15),id:'5513ca20-e577-11e9-8e9b-cf6e52d7d1e7',panelIndex:'3',type:visualization,version:'7.1.1'),(embeddableConfig:(),gridData:(h:15,i:'4',w:24,x:24,y:15),id:f4cd8790-e577-11e9-8e9b-cf6e52d7d1e7,panelIndex:'4',type:visualization,version:'7.1.1')),query:(language:kuery,query:''),timeRestore:!f,title:'New%20Dashboard',viewMode:view)

# es: https://search-lajc-wage-theft-oiaka2yn2mw4onwkkslm4oy4pa.us-east-1.es.amazonaws.com
# kibana: https://search-lajc-wage-theft-oiaka2yn2mw4onwkkslm4oy4pa.us-east-1.es.amazonaws.com/_plugin/kibana/
