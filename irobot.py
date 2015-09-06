import aiml
import os

brainfile = "bot-brain.brn"
learnings = "std-startup.xml"
cmd = "LOAD AIML B"
kernel = aiml.Kernel()

if os.path.isfile(brainfile):
  kernel.bootstrap(brainFile=brainfile)
else:
  kernel.bootstrap(learnFiles=learnings,commands=cmd)
  kernel.saveBrain(brainfile)


while(True):
  input = raw_input(">>>")
  if input=="exit":
    kernel.saveBrain(brainfile)
    exit()
  if input == "save":
    kernel.saveBrain(brainfile)
  if input == "delete":
    try:
      if os.path.exists(brainfile):
        os.remove(brainfile)
    except Exception,e:
      print(Exception," : ",e)
  else:
    print(kernel.respond(input))
