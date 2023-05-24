import argparse
import datetime
import random
from time import sleep

# Get human readable time to the millisecond
def get_hrtime():
    current_time = datetime.datetime.now()
    fr_time = current_time + datetime.timedelta(hours=2)
    timestamp = fr_time.strftime('%Y%m%d%H%M%S%f')[:-3]
    return timestamp

# Get and check script arguments
parser = argparse.ArgumentParser(description='Generate values following a random walk pattern')

parser.add_argument('--symbol', help='Stock symbol')
parser.add_argument('--output_path', help='Output path (default : ./in/<<symbol>>)')
parser.add_argument('--interval', help='Interval (milliseconds) before next value is generated (default : 100)')
parser.add_argument('--batch_size', help='Number of values per batch (default : 1). Values are outputed per batch.')
parser.add_argument('--max_iter', help='Maximum number of iterations (default : 100)')
parser.add_argument('--verbose', help='Prints processing log (default : False)')

args = parser.parse_args()

if args.symbol is None:
    exit("FATAL ERROR : argument <<symbol>> is mandatory (and it's the only one !)")
else :
    symbol = args.symbol

if args.output_path is None:
    output_path = f"./in/{symbol}"
else:
    output_path = int(args.output_path)

if args.interval is None:
    interval = 100
else:
    interval = int(args.interval)

if args.batch_size is None:
    batch_size = 1
else:
    batch_size = int(args.batch_size)

if args.max_iter is None:
    max_iter = 100
else:
    max_iter = int(args.max_iter)

if not args.verbose is None and args.verbose=="True":
    verbose = args.verbose
else:
    verbose = False

# Initialize randomnes and paths
walk_values = [-0.001, 0, 0.001]
random.seed("alpha_"+symbol)
alpha_value=round(random.uniform(100, 400), 2)

# Loops to generate values
batch_cur_index = 0
batch_data = ""
for i in range(0, max_iter):
    batch_cur_index += 1
    alpha_value += random.choice(walk_values)
    timestamp = get_hrtime()
    batch_data += timestamp+','+str(alpha_value)+'\n'
    if verbose:
        print(f"Iteration #{i}/{batch_cur_index} : {alpha_value:.3f}")
    if batch_cur_index == batch_size or i == max_iter:
        file_name = symbol+'_'+timestamp+'.csv'
        with open(f"{output_path}/{file_name}","w") as fp:
            fp.write(batch_data)
        batch_cur_index = 0
        batch_data = ""
        if verbose:
            print("Batch outputed")
    sleep(interval/1000)