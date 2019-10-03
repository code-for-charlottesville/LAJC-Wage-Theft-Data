# !/bin/python

from elasticsearch import Elasticsearch
import pandas as pd
import json
import logging
import sys

DATA_INDEX = 'claims'
DATA_FILE = '../Raw data/lajc_clean.csv'

USAGE = """
Indexes csv data from '{}' into an elastic 
search cluster under the index '{}'

USAGE: 
	python2.7 index_data.py [ELASTIC_SEARCH_ENDPOINT or --help]
""".format(DATA_FILE, DATA_INDEX)

if __name__ == '__main__':
    # parse args
    if len(sys.argv) != 2 or sys.argv[1] == "--help":
        print USAGE
        sys.exit(1)
    # init data file
    logging.basicConfig(filename="index.log", level=logging.DEBUG)
    logging.info("Reading in datafile: %s", DATA_FILE)
    claims_df = pd.read_csv(DATA_FILE)
    docs = json.loads(claims_df.to_json(orient='records'))
    esEndpoint = sys.argv[1]
    es = Elasticsearch([esEndpoint])
    logging.info("indexing to endpoint %s", esEndpoint)
    i = 0
    for doc in docs:
        doc_id = str(doc["claimID"])
        logging.info("indexing claimID: %s", doc["claimID"])
        i += 1
        print "indexing claim {} of {}".format(i, len(docs))
        es.index(index=DATA_INDEX,
                 doc_type='_doc',
                 id=doc_id,
                 body=json.dumps(doc))