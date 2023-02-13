import proxy

if __name__ == '__main__':
  proxy.main(plugins=['proxy.plugin.CacheResponsesPlugin', 'proxy.plugin.RedirectToCustomServerPlugin'])
