git filter-branch --env-filter '
    export GIT_AUTHOR_NAME="github-username"
    export GIT_AUTHOR_EMAIL="email@email.com"
' -- --branches --tags