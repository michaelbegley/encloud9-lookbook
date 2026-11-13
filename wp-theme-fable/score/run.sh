#!/bin/sh
# The whole scorecard for this build, in one go. Local test WordPress only.
# usage (from the repo root): sh wp-theme-fable/score/run.sh <wordpress dir> <out dir> [path to axe.min.js]
# 1 parity   wp-theme/score/shots.js + score.py (Claude's scorecard, unchanged, so both builds compare)
# 2 editing  score/editor-test.js (signs in as a throwaway Editor made by test-users.sh)
# 3 access   score/a11y.js (axe when its file is given, landmarks, focus, menu, speed numbers), WordPress and mock
set -e
WPD=${1:?wordpress dir}; OUT=${2:?out dir}; AXE=${3:-}
HERE=$(cd "$(dirname "$0")" && pwd); ROOT=$(cd "$HERE/../.." && pwd)
WPORT=${WPORT:-8090}; MPORT=${MPORT:-8091}
mkdir -p "$OUT"
curl -s -o /dev/null "http://localhost:$WPORT/" && curl -s -o /dev/null "http://localhost:$MPORT/site/" || sh "$HERE/serve.sh" "$WPD" $WPORT "$ROOT" $MPORT
export NODE_PATH=$(npm root -g)
node "$ROOT/wp-theme/score/shots.js" "$HERE/../content/pages.json" http://localhost:$MPORT/site http://localhost:$WPORT "$OUT/shots"
python3 -I "$ROOT/wp-theme/score/score.py" "$OUT/shots" "$WPD" | tee "$OUT/parity.json"
sh "$HERE/test-users.sh" "$WPD" "$OUT/test-users.json"
node "$HERE/editor-test.js" http://localhost:$WPORT "$OUT/test-users.json" "$OUT/editor.json" || true
node "$HERE/a11y.js" "$HERE/../content/pages.json" http://localhost:$WPORT "$OUT/a11y.json" "$AXE" http://localhost:$MPORT/site > "$OUT/a11y-summary.json"
echo "scorecard written to $OUT"
