import requests
import gzip
import shutil
import os

index_id = 'CC-MAIN-2022-05'
index_url = 'https://data.commoncrawl.org/crawl-data/'+index_id+'/cc-index.paths.gz'

### Utility Functions ###

# function to create file filtered by domain
def filter_by_domain(file, domain):
    # run SED command to filter file for lines that match domain
    os.system("sed -n '/"+domain+"/p' "+file+" > "+file+"."+domain+".filtered.txt")



# check to see if index_files folder exists
if os.path.exists('../index_files'):
    pass
else:
    os.mkdir('../index_files')

# check to see if cdx_files folder exists
if os.path.exists('../cdx_files'):
    pass
else:
    os.mkdir('../cdx_files')

# download data files

# check and see if '../index_files/'+index_id+'.gz' does not exist
if not os.path.exists('../index_files/'+index_id+'.gz'):
    # doesn't exist, download it
    req = requests.get(index_url)
    with open('../index_files/'+index_id+'.gz', 'wb') as f:
        f.write(req.content)
    with gzip.open('../index_files/'+index_id+'.gz', 'rb') as f_in:
        with open('../index_files/'+index_id+'.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

with open('../index_files/'+index_id+'.txt', 'r') as fin:
    cdx_files = fin.readlines()

#print number of items in cdx_files
print("Total lines:", len(cdx_files))

# loop over items in cdx_files
loops = len(cdx_files)
for i in range(0, loops):
    cdx_id = cdx_files[i].strip()
    cdx_url = 'https://data.commoncrawl.org/'+cdx_id
    cdx_fname = cdx_id.split('/')[-1].split('.')[0]
    
    # check to ../cdx_files/'+index_id+'/'+cdx_fname+'.txt' see if it exists
    output_filename = '../cdx_files/'+index_id+'/'+cdx_fname+'.txt'
    if not os.path.exists(output_filename):

        # download the file    
        print("Downloading:", cdx_fname)
        req = requests.get(cdx_url)

        # if ../cdx_files/'+index_id doesn't exist, create it
        if not os.path.exists('../cdx_files/'+index_id):
            os.mkdir('../cdx_files/'+index_id)
        
        with open('../cdx_files/'+index_id+'/'+cdx_fname, 'wb') as f:
            f.write(req.content)
        with gzip.open('../cdx_files/'+index_id+'/'+cdx_fname, 'rb') as f_in:
            with open(output_filename, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        # filter the downloaded file
        filter_by_domain(output_filename, 'msnbc.com')
        # optional, delete the source files after done filtering
        # os.remove('../cdx_files/'+index_id+'/'+cdx_fname)
        # os.remove(output_filename)


