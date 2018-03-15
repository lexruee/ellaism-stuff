#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alexander Rüedlinger'
__license__ = 'MIT'

import matplotlib.pyplot as plt
from helper import Client 
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import numpy as np
from dateutil.relativedelta import relativedelta
import math
import argparse
import sys


def create_diff_plot(dates, diffs):
    plt.plot(dates, diffs)
    plt.title('Ella Difficulty')
    plt.xlabel('Time')
    plt.ylabel('Difficulty in T')
    plt.yticks(np.arange(0, max(diffs) + 1, 0.5))

    datemin = min(dates) - relativedelta(days=+1)
    datemax = max(dates) + relativedelta(days=+1)

    plt.xlim(datemin, datemax)
    plt.gca().xaxis.set_minor_locator(mdates.DayLocator())
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    monthsFmt = DateFormatter("%b '%y")
    plt.gca().xaxis.set_major_formatter(monthsFmt)

    plt.gcf().autofmt_xdate()
    plt.grid()
    return plt 


if __name__ == '__main__':
    description = 'ellap - Simple tool to plot ella difficulty'
    version = '0.1'
    MAX_BLKS_PER_DAY = int(24 * 60 * 60 / 14)

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-V', '--version', action='version', 
            version='%(prog)s {}'.format(version), 
            help='Print version number.')
    parser.add_argument('-a', '--jsonrpc', dest='jsonrpc', 
            help='Set JSONRPC URL address.', default='http://localhost:8485')
    parser.add_argument('-s', '--start-block', dest='start_block', type=int,
            help='Set start block.', default=1)
    parser.add_argument('-e', '--end-block', dest='end_block', type=int,
            help='Set end block.', default=MAX_BLKS_PER_DAY * 30 * 4)
    parser.add_argument('-r', '--sampling-rate', dest='sampling_rate', type=float,
            help='Set sampling rate.', default=0.1)
    parser.add_argument('-o', '--output', dest='output', 
            help='Output file.', default='ella-diff.png')
    parser.add_argument('-S', '--show', dest='show', 
                help='Show plot.', action='store_true')
  
    args = parser.parse_args()

    
    block_step = int(args.sampling_rate * MAX_BLKS_PER_DAY)
    start_block, end_block = args.start_block, args.end_block
    
    try:
        client = Client(args.jsonrpc)
        blocks = client.get_blocks_from(start_block, end_block, block_step)
    except:
        print("Failed to fetch data from %s" % args.jsonrpc)
        sys.exit(1)

    diffs = [block['difficulty']/1000**4 for block in blocks]
    timestamps = [block['timestamp'] for block in blocks]
    dates = [datetime.fromtimestamp(int(t)) for t in timestamps]

    plt = create_diff_plot(dates, diffs)
 
    if args.output:
        plt.savefig(args.output)
    
    if args.show:
        plt.show()

