set -a
. .env_docker
set +a
echo "deploy market api platform stack $STACK_NAME"
docker build -t beemarket-api-platform-backend -f ./deploy/dockerfile/backend/Dockerfile .
docker stack deploy -c ./deploy/backend/docker-compose.yml "$STACK_NAME"
