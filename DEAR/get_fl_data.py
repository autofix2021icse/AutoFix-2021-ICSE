import os
import subprocess


path = os.getcwd()
projects = ["Chart", "Closure", "Lang", "Math", "Mockito", "Time"]
bugs = [26, 133, 65, 106, 38, 27]
folder = path + "/sbfl/defects4j_data"
subprocess.call("mkdir " + folder, shell=True)

for i in range(len(projects)):
    folder = path + "/sbfl/defects4j_data/" + projects[i]
    subprocess.call("mkdir " + folder, shell=True)

for i in range(len(projects)):
    for bug in range(bugs[i]):
        folder = path + "/sbfl/defects4j_data/" + projects[i] + "/" + str(bug+1)
        subprocess.call("mkdir " + folder, shell=True)

for i in range(len(projects)):
    for bug in range(bugs[i]):
        subprocess.call("defects4j checkout -p " + projects[i] + " -v " + str(bug+1) + "b -w " + folder, shell=True)
        os.chdir(path + "/sbfl/")
        subprocess.call("./sbfl.sh " + projects[i] + " " + str(bug+1) + " " + folder, shell=True)