#!/bin/bash

CONFIG_FILE=/usr/local/etc/redis/redis.conf

mkdir "$(dirname $CONFIG_FILE)"

rm -f $CONFIG_FILE
echo "bind 0.0.0.0" >>$CONFIG_FILE
if [[ -n $REDIS_PASSWORD ]]; then
  echo "requirepass $REDIS_PASSWORD" >>$CONFIG_FILE
fi

redis-server $CONFIG_FILE
