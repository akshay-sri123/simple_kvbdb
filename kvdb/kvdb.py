def kv_set(kv_dict, **kwargs):
    key = kwargs.get("key")
    value = kwargs.get("value")
    kv_dict[key] = value
    return kv_dict

def kv_get(kv_dict, **kwargs):
    key = kwargs.get("key")
    if key in kv_dict:
        return kv_dict.get(key)
    else:
        return None

def kv_del(kv_dict, **kwargs):
    key = kwargs.get("key")
    if key in kv_dict:
        _ = kv_dict.pop(key)
        return kv_dict
    else:
        return None

def kv_incr(kv_dict, **kwargs):
    key = kwargs.get("key")
    if key in kv_dict:
        kv_dict[key] = int(kv_dict[key]) + 1
    else:
        kv_dict[key] = 1
    return kv_dict[key]

def kv_incrby(kv_dict, **kwargs):
    key = kwargs.get("key")
    incr_by = kwargs.get("incr_by")
    if key in kv_dict:
        kv_dict[key] = int(kv_dict[key]) + incr_by
    else:
        kv_dict[key] = incr_by 
    return kv_dict[key]
