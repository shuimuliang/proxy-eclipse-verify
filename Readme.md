## install python package, global
```shell
pip3 install -r requirements.txt
```

## start proxy server
```
proxy --hostname 0.0.0.0 --plugins proxy.plugin.FilterByURLRegexPlugin --filtered-url-regex-config config.json
````

## test client
```
curl -x 127.0.0.1:8899 http://baidu.com
````

## plugin
https://github.com/abhinavsingh/proxy.py/tree/develop/proxy/plugin
https://github.com/abhinavsingh/proxy.py/blob/develop/proxy/plugin/modify_post_data.py
