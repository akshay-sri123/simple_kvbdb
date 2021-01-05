def kv_set(kv_dict, key, value):
    kv_dict[key] = value
    return kv_dict

def kv_get(kv_dict, key):
    if key in kv_dict:
        return kv_dict[key]
    else:
        return None

def kv_del(kv_dict, key):
    if key in kv_dict:
        _ = kv_dict.pop(key)
        return kv_dict
    else:
        return None

