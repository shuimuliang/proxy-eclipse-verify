# -*- coding: utf-8 -*-
"""
    proxy.py
    ~~~~~~~~
    ⚡⚡⚡ Fast, Lightweight, Pluggable, TLS interception capable proxy server focused on
    Network monitoring, controls & Application development, testing, debugging.

    :copyright: (c) 2013-present by Abhinav Singh and contributors.
    :license: BSD, see LICENSE for more details.

    .. spelling::

       localhost
       httpbin
"""
from typing import Optional

from ..http.proxy import HttpProxyBasePlugin
from ..http.parser import HttpParser
from ..http.exception import HttpRequestRejected
from ..http import httpStatusCodes
import json

class ModifyPostDataPlugin(HttpProxyBasePlugin):
    """Modify POST request body before sending to upstream server.

    Following curl executions will work:
        1. Plain
           curl -v -x localhost:8899 -X POST http://httpbin.org/post -d 'key=value'
        2. Chunked
           curl -v -x localhost:8899 -X POST \
               -H 'Transfer-Encoding: chunked' http://httpbin.org/post -d 'key=value'
        3. Chunked & Compressed
           echo 'key=value' | gzip | curl -v \
               -x localhost:8899 \
               -X POST \
               --data-binary @- -H 'Transfer-Encoding: chunked' \
               -H 'Content-Encoding: gzip' http://httpbin.org/post

    """

    MODIFIED_BODY = b'{"key": "modified"}'
    BannedMethod = ('requestAirdrop', 'sendTransaction', 'simulateTransaction') 

    def before_upstream_connection(
            self, request: HttpParser,
    ) -> Optional[HttpParser]:
        return request

    def handle_client_request(
            self, request: HttpParser,
    ) -> Optional[HttpParser]:
        content_type = request.headers.get(b'content-type')
        if content_type[1] == b'application/json':
            #print("hit content_type")
            if request.body:
                d = json.loads(request.body)
                #print(d)
                #print(ModifyPostDataPlugin.BannedMethod)
                if d['method'] in ModifyPostDataPlugin.BannedMethod:
                    raise HttpRequestRejected(
                        status_code=httpStatusCodes.INTERNAL_SERVER_ERROR,
                        reason=b'.',
                    )
        return request
