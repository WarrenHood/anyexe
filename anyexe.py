import ctypes, mmap, sys, os
def usage():
    print("Usage: jpexe.py filename")
if len(sys.argv) < 2:
    usage()
    sys.exit(0)
filename = sys.argv[-1]
outfile = filename[:filename.find(".")]+"_out.exe"
fin = open(filename,"rb")
bytecode = fin.read()
fin.close()
outf = open(r"C:\Users\\"+str(os.getlogin())+r"\\"+outfile,"wb")
outf.write(bytecode)
outf.close()
os.system(r"C:\Users\\"+str(os.getlogin())+r"\\"+outfile)
