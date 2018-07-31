# importing argparse module to take arguments from commandline
import argparse

# Create parser variable for pass command line arguments using ArgumentParser() function of argparse module 
parser = argparse.ArgumentParser()

# Arguments for the parser here
parser.add_argument("file", help="Specify a file")

# Grab all arguments
args = parser.parse_args()
	
# If user input file run program
if args.file:		

		# With command to open file for reading and read it as binary
		with open(args.file, 'r') as infile:
			
			offset=0
			
			while True:
			
				# read 16 characters from opened file and get that to text variable 
				text=infile.read(16)
				
				if not text:
					break
				else:
					hexlist=[]
					for charsfirst in text:
						decfirst = ord(charsfirst)
						hex = ('%02x'%decfirst)
						hexlist.append(hex)
					
					newhexlist=[]
					for hexas in range(0, len(hexlist), 2):
						newhexlist.append(''.join(hexlist[hexas:hexas+2]))
					
					charlist=[]
					for charssecond in text:
						decsecond = ord(charssecond)
						if(decsecond<32):
							charlist.append('.')
						else:
							charlist.append(charssecond)
				
				counter=offset*16
				offsethex=('%08x'%counter)
				
				print('{0}: {1:<39} {2}'.format(offsethex,' '.join(newhexlist),''.join(charlist)))
			
				offset = offset+1
				
# Else user not input file show massege in usage section 
else:
		
	print (parser.usage)
