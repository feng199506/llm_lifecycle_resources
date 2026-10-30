#!/usr/bin/env bash
# Not executed in the collection round.
set -euo pipefail
HERE=$(cd "$(dirname "$0")/.." && pwd)
KIT=$(cd "$HERE/../.." && pwd)
set -a
[ -f "$HERE/config/env.local" ] && . "$HERE/config/env.local" || . "$HERE/config/env.example"
set +a
BIN="${LLAMA_SERVER_BIN:-}"
if [ ! -x "${BIN:-}" ]; then
  CAND=$(find "$KIT/runtimes/linux_x86_64/llama_cpp" /root/ai_agent_resources/agent_runtime_kits/runtimes/linux_x86_64/llama_cpp -maxdepth 4 -type f -name 'llama-server' 2>/dev/null | head -n1 || true)
  BIN=${CAND:-}
fi
GGUF="${LLAMA_GGUF:-$KIT/models/cpu_baseline/qwen2.5-0.5b-instruct-q4_k_m.gguf}"
echo "binary=$BIN"
echo "gguf=$GGUF"
test -f "$GGUF"
test -x "$BIN"
exec "$BIN" -m "$GGUF" --port 8080 --host 127.0.0.1 -c "${LLAMA_CTX:-2048}" --alias "${LLM_MODEL:-qwen2.5-0.5b-instruct}"
