#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import LogMine

input_dir  = '../logs/HDFS/' # The input directory of log file
output_dir = 'LogMine_result/' # The output directory of parsing results
log_file   = 'frontend_logs1.txt' # The input log file name
log_format = '<Service> <IP> <Time> <Content>' # HDFS log format
levels     = 2 # The levels of hierarchy of patterns
max_dist   = 0.001 # The maximum distance between any log message in a cluster and the cluster representative
k          = 1 # The message distance weight (default: 1)
regex      = []  # Regular expression list for optional preprocessing (default: [])

parser = LogMine.LogParser(input_dir, output_dir, log_format, rex=regex, levels=levels, max_dist=max_dist, k=k)
parser.parse(log_file)
