# DEAR: A Novel Deep Learning-based Approach for Automated Program Repair

<p aligh="center"> This repository contains the code for <b>DEAR: A Novel Deep Learning-based Approach for Automated Program Repair</b> </p>

## Introduction ##

We present DEAR, a DL-based approach that supports auto-fixing for the bugs that could involve one or multiple hunks and one or multiple consecutive statements. We design an algorithm taking the buggy statements returned by a fault localization technique, to detect the buggy hunks and to expand a buggy statement in a hunk to include other suspicious consecutive statements from that statement. We design a two-tier, tree-based LSTM model that incorporates cycle training and uses a divide-and-conquer strategy to learn proper code transformations for fixing multiple statements in the suitable fixing context consisting of surrounding subtrees. We conducted several experiments to evaluate DEAR on three datasets: Defect4J (395 bugs), BigFix (+26k bugs), and CPatMiner (+44k bugs). DEAR is able to fix 47 bugs from Defects4J, including 7 multiple-statement bugs (15% of the total fixed bugs) that the state-of-the-art DL-based approaches cannot support. DEAR can outperform the state-of-the-art deep learning APR tools from 57%–683% in terms of the number of auto-fixed bugs with only Top-1 ranked patches on Defects4J. DEAR also achieves comparable and complementary results to the existing pattern-based APR approaches. 

----------

# The Dataset we used in the paper

Defects4J: https://github.com/rjust/defects4j

BigFix: https://github.com/OOPSLA-2019-BugDetection/OOPSLA-2019-BugDetection
Cleaned Version: https://drive.google.com/open?id=1KL3M-BbisVLWXyvn05V6huSLNUby_9qN

CPatMiner: https://nguyenhoan.github.io/CPatMiner/index.html
Cleaned Version: https://drive.google.com/open?id=1M_0dRYqhCMh26GQbnX4Igp_2jSrTS1tV  

----------

## Contents
1. [Dataset](#dataset)
2. [Requirement](#requirement)
3. [Code](#Code)
4. [Contact](#contact)



## Dataset

The Dataset we used in the paper

Defects4J: https://github.com/rjust/defects4j

BigFix: https://github.com/OOPSLA-2019-BugDetection/OOPSLA-2019-BugDetection
Cleaned Version: https://drive.google.com/open?id=1KL3M-BbisVLWXyvn05V6huSLNUby_9qN

CPatMiner: https://nguyenhoan.github.io/CPatMiner/index.html
Cleaned Version: https://drive.google.com/open?id=1M_0dRYqhCMh26GQbnX4Igp_2jSrTS1tV  

Before using our tool, please download the two clearned version of data and also setup the Defects4J. You can use /DEAR/sbfl/setup.sh to install Defects4J or manually install it, then you need to setup Defects4J and setup enviroment variable D4J_HOME that points to the install path of Defects4J.

Also, you need to download the pre-trained Bert model from https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip.

## Requirement

Please check all requirements in the requirement.txt

## Code

1. Clone our repository by using ```git clone https://github.com/autofix2021icse/AutoFix-2021-ICSE.git```

2. Put the downloaded clearned version of data in ```../DEAR/data``` and unzip it

3. Run get_fl_data.py to prepare data for fault localization and doing the fault localization

4. Run run_bert.sh to fine-tune the Bert (You need to fix the address in this file to make it match your local pretrained Bert model)

5. Modify the paramter RQ in main.py for running experiments in different RQs and doing evaluation for RQs.
