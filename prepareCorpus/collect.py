import requests
import gzip
import shutil
import os

index_id = 'CC-MAIN-2022-05'
index_url = 'https://data.commoncrawl.org/crawl-data/'+index_id+'/cc-index.paths.gz'

req = requests.get(index_url)
with open('../index_files/'+index_id+'.gz', 'wb') as f:
    f.write(req.content)
with gzip.open('../index_files/'+index_id+'.gz', 'rb') as f_in:
    with open('../index_files/'+index_id+'.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)



with open('../index_files/'+index_id+'.txt', 'r') as fin:
    cdx_files = fin.readlines()
cdx_id = cdx_files[0].strip()
cdx_url = 'https://data.commoncrawl.org/'+cdx_id
cdx_fname = cdx_id.split('/')[-1].split('.')[0]
req = requests.get(cdx_url)
if os.path.exists('../cdx_files/'+index_id):
    pass
else:
    os.mkdir('../cdx_files/'+index_id)
with open('../cdx_files/'+index_id+'/'+cdx_fname, 'wb') as f:
    f.write(req.content)
with gzip.open('../cdx_files/'+index_id+'/'+cdx_fname, 'rb') as f_in:
    with open('../cdx_files/'+index_id+'/'+cdx_fname+'.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)