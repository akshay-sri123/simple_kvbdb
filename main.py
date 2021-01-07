import sys
from kvdb.kvdb import kv_get, kv_del, kv_set, kv_incrby, kv_incr


def get_operations():
    return {
        "SET": kv_set,
        "GET": kv_get,
        "DEL": kv_del,
        "INCR": kv_incr,
        "INCRBY": kv_incrby
    }

if __name__ == "__main__":
    kvdb_dict = {}
    while True:
        command_input = input().split(" ")
        command = command_input[0]
        args = command_input[1:len(command_input)]
        if command in get_operations():
            operation = get_operations()[command]
            kwargs = {"key": args[0]}
            if command in ["SET"]:
                kwargs = {"key": args[0], "value": args[1]} 
            
            print(operation(kvdb_dict, **kwargs))
        else:
            print("Operation not defined.")
