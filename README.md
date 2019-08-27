# DevOpsChallenge
# About
A python script check_file.py that will accept an argument.
A python script test_redis.py that will connect to Redis cache.

# Usage
To run script 
>> python check_file.py -s <File_directory>
It will change all the filename of the files in a directory to
small letter

>> python check_file.py -s <File_directory>
It will change all the filename of the files in a directory to
capital letter

>> python test_redis.py -redis_host 172.24.1.10 -redis_port 27017 -redisdb 0
It will connect to the redis cache and print the ping result to show connection success.

