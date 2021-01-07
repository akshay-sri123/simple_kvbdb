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
        kv_dict[key] = int(kv_dict[key]) + int(incr_by)
    else:
        kv_dict[key] = incr_by 
    return kv_dict[key]


def kv_execute_multiline(kv_dict, multiline_commands):
    if multiline_commands[0] == "MULTI":
        if multiline_commands[-1] == "EXEC":
            for command in multiline_commands[1:len(multiline_commands)-1]:
                kv_execute(kv_dict, command)
        if multiline_commands[-1] == "DISCARD":
            pass

    return kv_dict


def kv_execute(kvdb_dict, input_command):
    command_input = input_command.split(" ")
    command = command_input[0]
        
    args = command_input[1:len(command_input)]
    if command in get_operations():
        operation = get_operations()[command]
            
        kwargs = {"key": args[0]}
        if command in ["SET"]:
            kwargs = {"key": args[0], "value": args[1]}
        if command in ["INCRBY"]: 
            kwargs = {"key": args[0], "incr_by": args[1]}
            
        print(operation(kvdb_dict, **kwargs))
    else:
        print("Operation not defined.")

def kv_compact(kv_dict):
    compacted_command = []
    for key, value in kv_dict.items():
        compacted_command.append("SET {} {}".format(key, value))
    return compacted_command

def get_operations():
    return {
        "SET": kv_set,
        "GET": kv_get,
        "DEL": kv_del,
        "INCR": kv_incr,
        "INCRBY": kv_incrby,
        "COMPACT": kv_compact
    }
