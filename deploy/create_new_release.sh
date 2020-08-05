#!/usr/bin/env bash

set -e

if ! git config --list | grep fetch | grep notes &>/dev/null; then
	git config --add remote.origin.fetch '+refs/notes/*:refs/notes/*'
fi
git fetch

declare CURRENT_VERSION=$(stepup version show)
echo $CURRENT_VERSION | grep '+' &>/dev/null || { echo "Current release $CURRENT_VERSION"; exit 0; }

declare WHATS_NEW=$(stepup notes show | grep -v '\---')
[ $(wc -l <<<"$WHATS_NEW") -ge 2 ] || { echo "No notes on $CURRENT_VERSION to increase version."; exit 1; }

declare NEXT_VERSION=$(stepup version show --next-release)

# se a tag com essa versao jah existe, entao tenta seguir para a proxima
if git show refs/tags/$NEXT_VERSION &>/dev/null; then
	NEXT_VERSION=$(echo $NEXT_VERSION | stepup version show --next-release)
fi

curl -v \
  --header "PRIVATE-TOKEN: $GITLAB_PVT_TOKEN" \
  --data-urlencode "tag_name=$NEXT_VERSION" \
  --data-urlencode "ref=$(git rev-parse HEAD)" \
  --data-urlencode "message=$WHATS_NEW" \
  --data-urlencode "release_description=$WHATS_NEW" \
  "https://gitlab.com/api/v4/projects/$CI_PROJECT_ID/repository/tags"

