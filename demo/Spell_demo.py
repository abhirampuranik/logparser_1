#!/usr/bin/env python
import sys
import time
sys.path.append('../')
from logparser import Spell

input_dir  = '../logs/HDFS/'  # The input directory of log file
output_dir = 'Spell_result/'  # The output directory of parsing results
log_file   = 'HDFS_2k.log'  # The input log file name
log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>'  # HDFS log format
tau        = 0.5  # Message type threshold (default: 0.5)
regex      = []  # Regular expression list for optional preprocessing (default: [])


start = time.time()
parser = Spell.LogParser(indir=input_dir, outdir=output_dir, log_format=log_format, tau=tau, rex=regex)
parser.parse(log_file)

end = time.time()
print(end - start)

