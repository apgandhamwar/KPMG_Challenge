from functools import reduce

def deep_get(_dict, keys, default=None):

    def _reducer(d, key):
        if isinstance(d, dict):
            
               
            return d.get(key, default)
        return default
    
    keysspt = keys.split('/')
    return reduce(_reducer, keysspt, _dict)




object = {'x':{'y':{'z':{'b':'a'}}}}

print (deep_get(object, 'x/y/z/b'))