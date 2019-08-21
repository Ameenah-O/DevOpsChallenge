# imports
import argparse
import redis

#Parser to fetch command line arguements
parser = argparse.ArgumentParser()
parser.add_argument("-redis_host",required=True)
parser.add_argument("-redis_port",required=True)
parser.add_argument("-redisdb")
parser.add_argument("-redis_password")
parser.add_argument("-redis_ssl",default=True)
args = parser.parse_args()



redis_conection = redis.Redis(host=args.redis_host, port=args.redis_port,ssl=args.redis_ssl, password=args.redis_password)

#Test conection
result = redis_conection.ping()
print("Ping returned : " + str(result))
