#proxy --hostname 0.0.0.0 --log-level d --plugins proxy.plugin.RedirectToCustomServerPlugin

proxy --hostname 0.0.0.0 \
  --disable-http-proxy \
  --log-level d \
  --plugins proxy.plugin.RedirectToCustomServerPlugin

#  --enable-web-server \
