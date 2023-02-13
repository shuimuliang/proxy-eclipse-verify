## 1. 安装proxy.py依赖包, install python package, global
```shell
pip3 install -r requirements.txt
```

## 查找proxy.py安装目录
```
pip3 show proxy.py 
#Location: /opt/homebrew/lib/python3.10/site-packages
```

## 用modify_post_data.py覆盖文件
/opt/homebrew/lib/python3.10/site-packages/proxy/plugin/modify_post_data.py

## 启动foward proxy, 并加载插件, start proxy server
filter header 'Content-Type: application/json'
filter post body method in ('requestAirdrop', 'sendTransaction', 'simulateTransaction')
```
proxy --hostname 0.0.0.0 --threadless --plugins proxy.plugin.ModifyPostDataPlugin
````

## test client
```
curl -x 127.0.0.1:8899 http://baidu.com --header 'Content-Type: application/json' --data-raw '{"jsonrpc": "2.0", "method": "get_slot_height", "id": 2}'
curl -x 127.0.0.1:8899 http://baidu.com --header 'Content-Type: application/json' --data-raw '{"jsonrpc": "2.0", "method": "simulateTransaction", "id": 2}'
````

## plugin reference
https://github.com/abhinavsingh/proxy.py/tree/develop/proxy/plugin
https://github.com/abhinavsingh/proxy.py/blob/develop/proxy/plugin/modify_post_data.py
