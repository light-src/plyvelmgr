# ICON DB TOOLS

* Use plyvel with Cli


# Commands

* [getbykey](#getbykey)
* [setbykey](#setbykey)
* [erasebykey](#erasebykey)
* [checkdiff](#checkdiff)


## getbykey

* get value in db by key

```bash
(venv) $ plyvelmgr getbykey --help
usage: plyvelmgr getbykey [-h] --db DB --key KEY

optional arguments:
  -h, --help  show this help message and exit
  --db DB
  --key KEY
 

(venv) $ plyvelmgr getbykey --db sync3/.statedb/icon_dex/ --key 696973736d64
b'\x96\x00\xcc\xc8\xcd\x04\xb0\xcd\x1bX\xce\x00\x03K\xc0\xce\x00\r/\x00'
```

| key | value | desc |
|:----|:-----:|------|
| --db | string| the path of plyvel db|
| --key| string| key value|


## setbykey
* set value in db with key
* remain log in cur_path/plyvelmgr.log

```bash
(venv) $ plyvelmgr setbykey --help
usage: plyvelmgr setbykey [-h] --db DB --key KEY --value VALUE

optional arguments:
  -h, --help     show this help message and exit
  --db DB
  --key KEY
  --value VALUE
  
(venv) $ plyvelmgr setbykey --db sync3/.statedb/icon_dex/ --key 696973736d65 --value 969673736d65
db set 696973736d65 : 969673736d65
```

| key | value | desc |
|:----|:-----:|------|
| --db | string| the path of plyvel db|
| --key| string| key value|
| --value| string| value|

## erasebykey
* erase unit in db
* remain log in cur_path/plyvelmgr.log

```bash
(venv) $ plyvelmgr erasebykey --help
usage: plyvelmgr erasebykey [-h] --db DB --key KEY

optional arguments:
  -h, --help  show this help message and exit
  --db DB
  --key KEY
  
(venv) $ plyvelmgr erasebykey --db sync3/.statedb/icon_dex/ --key 696973736d65
db erased 696973736d65
```
| key | value | desc |
|:----|:-----:|------|
| --db | string| the path of plyvel db|
| --key| string| key value to erase|

## checkdiff
* check differences comparing two db.
* remain log in cur_path/plyvelmgr_diff_check.log
```bash
(venv) $ plyvelmgr checkdiff --help
usage: plyvelmgr checkdiff [-h] --db DB --cmp-db CMP_DB

optional arguments:
  -h, --help       show this help message and exit
  --db DB
  --cmp-db CMP_DB

(venv) $ plyvelmgr checkdiff --db sync3/.statedb/icon_dex/ --cmp-db mycom22/7533273/.score_data/db/icon_dex/
checking iterator size
19787437
checking iterator size
19787434
diff_checking...
diff_detected!
b'iissmd'
diff_detected!
b'iisspk'
diff_detected!
b'prepprf'
```
| key | value | desc |
|:----|:-----:|------|
| --db | string| the path of plyvel db|
| --cmp-db| string| the path of plyvel db to compare|

