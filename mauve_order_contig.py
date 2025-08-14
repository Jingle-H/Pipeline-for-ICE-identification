import os
import sys
import linecache as lc
from itertools import islice
from multiprocessing.pool import Pool
import time

##the file of ref_genome should be gbk, such as the gbk file generated using prokka.
 
fullpath_Mauve='/path/to/mauve/'
ref_path='/path/to/ref_genome/'
MAG_path='/path/to/your_MAG/'
mauve_out_path='/path/to/mauve_result/'
query_file='/path/to/query_ref_list.txt'

def mauve(draft,ref,ref_path):
	os.chdir(fullpath_Mauve)
	os.system('cp '+ref_path+ref+'_prokka/'+ref+'_prokka.gbk '+fullpath_Mauve)
	os.system('cp '+MAG_path+draft+' '+fullpath_Mauve)
	#draft_genome=draft.split('/')[-1]
	os.system('java -Xmx500m -cp Mauve.jar org.gel.mauve.contigs.ContigOrderer -output '+draft+'--'+ref+'--mauve_result -ref '+ref+'_prokka.gbk -draft '+draft)
	os.system('mv '+draft+'--'+ref+'--mauve_result '+mauve_out_path)
	os.system('rm '+fullpath_Mauve+ref+'_prokka.gbk')
	os.system('rm '+fullpath_Mauve+draft)
	

if __name__ == '__main__':	
	fin=open(query_file,'r')
	d={}
	l_ref=[]
	for line in fin:
		qry=line.strip().split('\t')[0]
		ref=line.strip().split('\t')[-1]
		l_ref.append(ref)
		if qry not in d.keys():
			d[qry]=[]
			d[qry].append(ref)
		else:
			d[qry].append(ref)
		

	pool=Pool(processes=20)
	for item in d.keys():
		for item2 in d[item]:
			pool.apply_async(mauve,args=(item+'.fa',item2,ref_path))
	pool.close()
	pool.join()

	