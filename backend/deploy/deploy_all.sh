set -a
. .env_docker
set +a

# build and deploy redis
echo "build redis image..."
docker build -t beemarket-api-platform-redis -f ./deploy/dockerfile/redis/Dockerfile .
echo "deploy redis stack $STACK_NAME, data folder: $REDIS_DATA_PATH"
docker stack deploy -c ./deploy/redis/docker-compose.yml "$STACK_NAME"

# deploy postgres
echo "deploy postgres stack $STACK_NAME, data folder: $POSTGRES_DATA_PATH"
docker stack deploy -c ./deploy/postgres/docker-compose.yml "$STACK_NAME"
