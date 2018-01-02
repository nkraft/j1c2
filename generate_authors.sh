#!/bin/bash

declare -r authors_dir="$(pwd)/authors"
declare -ar venues=(software fse icse)

generate_authors() {
  local venue authors_glob cmd
  venue="$@"
  authors_glob="${authors_dir}/${venue}*.txt"
  cmd="cat ${authors_glob} | sort | uniq > ${authors_dir}/${venue}.txt"
  echo "${cmd}"
  eval "${cmd}"
}

main() {
  for venue in "${venues[@]}"; do
    generate_authors "${venue}"
  done
}

main "$@"

