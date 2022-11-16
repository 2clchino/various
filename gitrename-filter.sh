git filter-branch -f --env-filter '
    if test "$GIT_AUTHOR_NAME" = "mano"
    then
        GIT_AUTHOR_EMAIL="mano.24.rites@gmail.com"
        GIT_AUTHOR_NAME="cl2chino"
    fi
    if test "$GIT_COMMITTER_NAME" = "mano"
    then
        GIT_COMMITTER_EMAIL="mano.24.rites@gmail.com"
        GIT_COMMITTER_NAME="cl2chino"
    fi' --tag-name-filter cat HEAD
