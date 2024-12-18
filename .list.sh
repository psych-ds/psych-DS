#!/bin/bash

shopt -s dotglob nullglob globstar

for file in **; do
    ls --directory --classify --color=yes -- "$file"
    filetype="$(file --brief --mime-type -- "$file")"
    # Only print text files
    if [[ $filetype == text/* ]]; then
        printf '\e[32m==> %s %s <==\e[m\n' start "$file"
        cat --show-nonprinting -- "$file"
        printf '\e[31m==> %s %s <==\e[m\n' end "$file"
        echo
    fi
done
