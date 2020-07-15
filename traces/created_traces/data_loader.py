import numpy as np
from scipy import signal
import argparse
import matplotlib.pyplot as plt


import pandas as pd

def load_and_display_file(file, decimation_factor = 10):
    trace = np.load(file)
    #filtering the trace to make differences more visible

    trace = signal.decimate(trace,decimation_factor)
    plt.plot(trace)
    plt.ylabel("V")
    plt.xlabel("Sample")
    plt.title("Artificial Bulk Power Trace")
    
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage="Test application to parse a trace binary file")
    parser.add_argument(
        "-t", "--trace_data_file",
        type=str,
        help="Path to the trace data file",)
    parser.add_argument(
    "-d", "--decimation_factor",
    type=int,
    default=10,
    help="Decimate the trace by a factor to save computation time (defaults to 10)",)
    arguments = parser.parse_args()
    
    if arguments.trace_data_file is not None:
        load_and_display_file(arguments.trace_data_file,arguments.decimation_factor)
    else:
        print("No File input. Exit application!")