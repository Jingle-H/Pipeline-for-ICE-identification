import os
import sys
import linecache as lc
from itertools import islice
from multiprocessing.pool import Pool
import time

data_dir='/path/to/unordered_CONJ_MAG/GI/GI_with_CONJ/'
aa_dir='/path/to/unordered_CONJ_MAG/GI/'
os.system('mkdir '+data_dir+'int_result')
out_dir=data_dir+'int_result/'

def chunk_list(filelist,limit):
    filelist=iter(filelist)
    return iter(lambda: list(islice(filelist,limit)),[])



def int_hmm(file):
    int_hmm_l=['PF00589','PF00665','PF06782','PF07508']
    for item in int_hmm_l:
        os.system('hmmsearch --tblout '+out_dir+file+'_'+item+'.txt /path/to/int_hmm/'+item+'_seed.hmm '+aa_dir+file+'_ORF.aa')
    return


if __name__ == '__main__':
    time1=time.time()
    current_pwd=os.getcwd()
    dir_list=os.listdir(current_pwd)
    D=[]
    for item in dir_list:
        if item.endswith('.fa'):

            D.append(item)
    for temp_list in chunk_list(D,20):
        pool=Pool(processes=20)
        result=pool.map(int_hmm,temp_list)
        pool.close()
        pool.join()
    time2=time.time()
    print('T: '+str(time2-time1))
