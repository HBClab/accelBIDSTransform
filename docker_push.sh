echo "$DOCKER_PASS" | docker login --username "$DOCKER_USERNAME" --password-stdin
# if tag is defined
if [[ ! -z "$TRAVIS_TAG"]]; then
    docker push hbclab/accel-bids:$TRAVIS_TAG
# if the build is on the master branch
elif [[ "$TRAVIS_BRANCH" == "master" ]]; then
    docker push hbclab/accel-bids:unstable
else
    echo "This build is not on the master branch or a tagged release"
