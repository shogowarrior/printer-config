# GIT tips

## Reset git commit author
```sh
git filter-branch --env-filter '
    export GIT_AUTHOR_NAME="New Author Name"
    export GIT_AUTHOR_EMAIL="new-email@example.com"
' -- --branches --tags
```