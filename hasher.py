import argparse
import csv
import hashlib

#command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('input', help='input file or string')
parser.add_argument('-s', '--string', help='string of ciphertext', action='store_true')
parser.add_argument('-f', '--file', help='text file of ciphertext', action='store_true')
args = parser.parse_args()

def string_hash(plaintext):
	hash_list = []
	hash_list.append(["md5", hashlib.md5(plaintext).hexdigest()])
	hash_list.append(["sha1", hashlib.sha1(plaintext).hexdigest()])
	hash_list.append(["sha256", hashlib.sha256(plaintext).hexdigest()])
	hash_list.append(["sha512", hashlib.sha512(plaintext).hexdigest()])
	return hash_list

def file_hash(filename):
	fh_md5 = hashlib.md5()
	fh_sha1 = hashlib.sha1()
	fh_sha256 = hashlib.sha256()
	fh_sha512 = hashlib.sha512()
	
	with open(filename, 'rb') as file:
		buff = file.read()
		
		fh_md5.update(buff)
		fh_sha1.update(buff)
		fh_sha256.update(buff)
		fh_sha512.update(buff)
	
	
	return [["md5", fh_md5.hexdigest()], ["sha1", fh_sha1.hexdigest()], ["sha256", fh_sha256.hexdigest()], ["sha512", fh_sha512.hexdigest()]]
		

def write_opt(opt, inp):
	#Potentially name file/string csv automatically.  Security issues though.
	#if args.file:
	#	new = inp.split(".")
	#	inp = new[0]
	
	with open("hashed.csv", 'w') as f:
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow([inp])
		writer.writerows(opt)
	return None


	
hashlist = ["md5", "sha1", "sha256", "sha512"]
message = args.input
opt = []
def main():
	if args.string:
		opt = string_hash(message.encode('utf-8'))
		write_opt(opt, message)
		exit()
	if args.file:
		opt = file_hash(message)
		write_opt(opt, message)
		exit()
	else:
		print("please specify -s or -f")
		print("Usage: ./hasher.py [input] -sf [optional flags]")
		exit()


#opt.append([h, __import__(h, fromlist=['*']).string_hash(message.encode('utf-8'))])

if __name__ == '__main__':
	print("--Hashing tool by Mitch--")
	main()