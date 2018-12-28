import re
import sys
from collections import Counter

def analyzer(file_name='auth.log'):
    data = Counter()
    apps = []

    # Read logfile
    with open(file_name) as f:
        for line in f.readlines():
            time = line[:12]
            token = re.split(r'\s+', line)[4]
            app = re.sub(r'[^a-z]', '', token, flags=re.IGNORECASE)
            if app not in apps:
                apps.append(app)
            if time not in data:
                data[time] = Counter()
            data[time]['count'] += 1
            data[time][app] += 1

    # Print header
    print('time,count,{}'.format(','.join(apps)))

    # Print data
    for k, v in sorted(data.items()):
        line = '{},{}'.format(k, v['count'])
        for app in apps:
            try:
                line += ',{}'.format(data[k][app])
            except:
                line += ',0'
        print(line)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        analyzer(sys.argv[1])
    else:
        analyzer()

