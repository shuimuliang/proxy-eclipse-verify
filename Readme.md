# curl -x proxy方式
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
## 用redirect_to_custom_server.py覆盖文件
/opt/homebrew/lib/python3.10/site-packages/proxy/plugin/redirect_to_custom_server.py
## 修改redirect_to_custom_server.py中
UPSTREAM_SERVER = "http://origin-domain:port"

## 启动foward proxy, 并加载插件, start proxy server
filter header 'Content-Type: application/json'
filter post body method in ('requestAirdrop', 'sendTransaction', 'simulateTransaction')
```
proxy --hostname 0.0.0.0 --threadless --plugins proxy.plugin.ModifyPostDataPlugin --plugins proxy.plugin.RedirectToCustomServerPlugin
````

## test client
```
curl http://localhost:8899 -X POST -H "Content-Type: application/json" -d '
  {
    "jsonrpc":"2.0","id":1,
    "method":"getBlockHeight"
  }
'
curl http://localhost:8899 -X POST -H "Content-Type: application/json" -d '
  {
    "jsonrpc":"2.0","id":1,
    "method":"simulateTransaction"
  }
'
````

## plugin reference
https://github.com/abhinavsingh/proxy.py/tree/develop/proxy/plugin
https://github.com/abhinavsingh/proxy.py/blob/develop/proxy/plugin/modify_post_data.py

# forward proxy方式
python3 server.py
