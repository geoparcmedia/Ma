import json,sys
d=json.load(open('out/%s.json'%sys.argv[1]))
print(json.dumps(d['fields'],ensure_ascii=False));print('=====');print(json.dumps(d['meta_input'],ensure_ascii=False))
