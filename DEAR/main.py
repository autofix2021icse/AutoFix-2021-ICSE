import os
import time
import subprocess


rq = "1"
path = os.getcwd()
start = time.process_time()
if os.path.isdir(path + "/sbfl/ochiai/") and  os.path.isdir(path + "bert_model/bert_output/"):
    try:
        subprocess.call("python3 " + path + "run_exp.py " + rq, shell=True)
    except:
        print("Running Error!")
else:
    print("You need to finish the previous steps for preparing!")
time_length = time.process_time() - start
print("Cost " + str(time_length) + " s to finish the model")
