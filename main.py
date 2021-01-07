import sys
from kvdb.kvdb import kv_get, kv_del, kv_set, kv_incrby, kv_incr, kv_execute, kv_execute_multiline, kv_compact

if __name__ == "__main__":
    kvdb_dict = {}
    
    while True:
        input_command = input()
        if "COMPACT" in input_command:
            for compacted in kv_compact(kvdb_dict):
                print(compacted)
        elif "MULTI" in input_command:
            multiline_commands = []
            multiline_commands.append(input_command)
            multiline = True
            while multiline:
                multiline_input = input()
                if multiline_input in ["EXEC", "DISCARD"]:
                    multiline = False
                        
                multiline_commands.append(multiline_input)
            kv_execute_multiline(kvdb_dict, multiline_commands)
        else:        
            kv_execute(kvdb_dict, input_command)
