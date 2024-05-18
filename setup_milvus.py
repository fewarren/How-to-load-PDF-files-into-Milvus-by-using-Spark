import os
from pymilvus import connections, Collection, utility
from dotenv import load_dotenv
load_dotenv()

def init_vectordb():
    HOST = os.getenv('MILVUS_HOST')
    PORT = os.getenv('MILVUS_PORT')
    # Connect to Milvus Database
    connections.connect(host=HOST, port=PORT, secure=False)
    
    print('Opening collection and index for "%s"' % collection_name)
    collection = Collection('MILVUS_COLLECTION_NAME')      # Get an existing collection.
    collection.load()
    return collection

if __name__ == '__main__':
    init_vectordb()
