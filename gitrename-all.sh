git filter-branch -f --env-filter "GIT_AUTHOR_NAME='cl2chino'; GIT_AUTHOR_EMAIL='mano.24.rites@gmail.com'; GIT_COMMITTER_NAME='cl2chino'; GIT_COMMITTER_EMAIL='mano.24.rites@gmail.com';" --tag-name-filter cat HEAD