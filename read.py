open_file=open('/var/lib/jenkins/workspace/My_Job2/port.py','r')
read=open_file.read()
for a in read:
  if a.isnumeric() == True: 
      print(a,end='')
