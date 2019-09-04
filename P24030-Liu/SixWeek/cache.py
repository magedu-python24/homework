import time
import functools
import inspect

def cache(fn):
    cache={}
    @functools.wraps(fn)
    def wapper(*args,**kwargs):
        sig=inspect.signature(fn)
        params=sig.parameters
        param_names=[k for k in params.keys()]

        param_dict={}
        for i,v in enumerate(args):
            param_dict[param_names[i]]=v
        param_dict.update(kwargs)

        for k,v in params.items():
            if k not in param_dict.keys():
                param_dict[k] = v.default
        key=tuple(sorted(param_dict.items()))

        if key not in cache.keys():
            cache[key]=fn(*args,**kwargs)
        return cache[key]
    return wapper

@cache
def add(x=4,y=5):
    time.sleep(2)
    return x+y;

print(add())
print(add(4,5))
print(add(4,y=5))
print(add(4,6))
