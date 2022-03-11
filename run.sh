#/bin/bash

VOL1=data/rabbitmq/log
VOL2=data/rabbitmq/data
mkdir -p "$VOL1"
mkdir -p "$VOL2"

FILE=.bash_profile

if [[ ! -f "$FILE" ]]
then
  echo 'export DOCKER_USER="$(id -u):$(id -g)"' >>  "$FILE"
  echo 'export VOL1="$VOL1"' >>  "$FILE"
fi

source "$FILE"

docker-compose -f docker/docker-compose.yml up -d

python auth/runner.py