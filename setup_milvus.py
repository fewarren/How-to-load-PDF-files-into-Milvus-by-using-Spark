import os
from pymilvus import connections, Collection
from dotenv import load_dotenv
load_dotenv()

def init_vectordb():
    if os.path.exists('setup.cfg'):
        print('Found config file')

    HOST = os.getenv('MILVUS_HOST')
    PORT = os.getenv('MILVUS_PORT')
    # Connect to Milvus Database
    connections.connect(host=HOST, port=PORT, secure=False)
    
    print('Opening collection and index for "%s"' % 'MILVUS_COLLECTION_NAME')
    collection = Collection('MILVUS_COLLECTION_NAME')      # Get an existing collection.
    collection.load()
    return collection

if __name__ == '__main__':
    init_vectordb()
