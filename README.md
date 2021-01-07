# simple_kvbdb

- Wrote down empty functions, added failing test cases for them, then updated functions
- Adding increment operations did not require much changes, just added the functions with test cases, then added operations in kv_execute and get_operations
    - For incrby, had to make sure of types (both int)
- For multiline, had to move the kv_execute to kvdb.py and updated it to take in a command line at a time and then split and execute
    - and kv_multiline to basically take in array and then execute line by line or not
- Had to add some logic to main to generate the array
- Not much for compacted, just updated the main with a condition
