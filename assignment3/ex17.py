from sys import argv
from os.path import exists

scrip, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line
in_file = open(from_file)
indata = in_file.read()
#indata = open(from_file).read()

#print(f"This input file is {len(indata)} bytes long")

#print(f"Does the output file exists? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

#open(argv[2],'w').write(in_file.read(open(argv[1]))
