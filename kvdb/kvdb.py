def kv_set(kv_dict, **kwargs):
    key = kwargs.get("key")
    value = kwargs.get("value")
    kv_dict[key] = value
    return kv_dict

def kv_get(kv_dict, **kwargs):
    key = kwargs.get("key")
    if key in kv_dict:
        return kv_dict[key]
    else:
        return None

def kv_del(kv_dict, **kwargs):
    key = kwargs.get("key")
    if key in kv_dict:
        _ = kv_dict.pop(key)
        return kv_dict
    else:
        return None

