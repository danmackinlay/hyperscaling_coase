import json,sys
for line in open(sys.argv[1]):
    if line.startswith('{'):
        d=json.loads(line)
        lab=d['label'].split('(')[0]
        print(f"{lab:22s} interim {d['interim']}\n{'':22s} realised {d['realised_types']} NPgain {d['nash_realised_gains']} floor {d['floor_realised']} Esurp {d['exp_surplus']} exante {d['exante']} resshare {d['res_share_exante']} expost@true {d.get('expost_true')} {d.get('schedule_true')} repl {d['replaceable_on']}")
    elif line.startswith('====='): print(line.strip())
