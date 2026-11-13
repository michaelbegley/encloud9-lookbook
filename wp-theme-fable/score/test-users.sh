#!/bin/sh
# Makes two throwaway local test users (an Editor and an Admin) for the editor test and writes their
# generated passwords to a file OUTSIDE the repo. Local test WordPress only; never run on a real site.
# usage: sh test-users.sh <wordpress dir> <secrets file>
WPD=$1; OUT=$2
WP="php $(dirname "$WPD")/wp-cli.phar --allow-root --path=$WPD"
case "$($WP option get home 2>/dev/null)" in http://localhost:*|http://127.0.0.1:*) ;; *) echo "not a local test site, stopping"; exit 1;; esac
umask 077
E1=$(openssl rand -hex 16); A1=$(openssl rand -hex 16)
for u in n9-test-editor:editor:$E1 n9-test-admin:administrator:$A1; do
  name=${u%%:*}; rest=${u#*:}; role=${rest%%:*}; pass=${rest#*:}
  $WP user get $name --field=ID >/dev/null 2>&1 || $WP user create $name $name@example.com --role=$role --porcelain >/dev/null 2>&1
  $WP user update $name --user_pass=$pass --skip-email >/dev/null 2>&1
done
printf '{"editor":{"user":"n9-test-editor","pass":"%s"},"admin":{"user":"n9-test-admin","pass":"%s"}}\n' "$E1" "$A1" > "$OUT"
echo "test users ready"
