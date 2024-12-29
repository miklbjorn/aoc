import requests
import argparse
import datetime
import os
import shutil
import sys
from pathlib import Path

SESSION_ID = os.environ['AOC_SESSION_ID']
BASE_PATH = Path(__file__).parent
TEMPLATE_FILE = BASE_PATH / 'template.py'

parser = argparse.ArgumentParser()
parser.add_argument('-y', default=None)
parser.add_argument('-d', default=None)
args = parser.parse_args()

now = datetime.datetime.now()
year = args.y
day = args.d
if (year is None or day is None) and now.month != 12:
    raise Exception('Can ONLY do automatic date parsing in December!')
else:
    year = str(year if year else now.year).rjust(4, '0')
    day = str(day if day else now.day).rjust(2, '0')
print(f'Setting AOC up for: {day}-12-{year}!')

# some years are special cases ...
if year == '2019':
    print('2019 is handled as a rust package - check 2019 folder!')
    sys.exit()

path = BASE_PATH / year / day
os.makedirs(path, exist_ok=False)
shutil.copyfile(TEMPLATE_FILE, path / f'{year}_{day}.py')

cookies = {'session': SESSION_ID}
r = requests.get(f"https://adventofcode.com/{year}/day/{int(day)}/input", cookies = cookies)
with open(path / 'input', 'w') as f:
    f.write(r.text)