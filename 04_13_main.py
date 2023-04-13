ecg = {}

with open("input.txt", 'r') as f:
    for line in f:
        if 'ecg' in line:
            # {"timestamp": 1678898291835, "leadOff": 1, "ecg": 3920}\n
            l_new = line.strip().strip('{}').split(',')
            # [
            #       '"timestamp": 1678898291835',
            #       ' "leadOff": 1',
            #       ' "ecg": 3920',
            # ]
            found_ts = False
            found_ecg = False
            for e in l_new:
                k, v = [i.strip('" ') for i in e.strip().split(':')]
                if k == 'timestamp':
                    found_ts = True
                    key = int(v)
                if k == 'ecg':
                    found_ecg = True
                    value = int(v)

            if found_ts and found_ecg:
                ecg[key] = value

print(str(ecg).replace(', ', ',\n'))

