FROM redis:6.0.5
COPY ./deploy/dockerfile/redis/entrypoint.sh   /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
ENV     REDIS_PASSWORD               ""
ENTRYPOINT [ "entrypoint.sh" ]