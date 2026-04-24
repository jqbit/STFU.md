#!/usr/bin/env node
const fs = require('fs');
const { get_encoding } = require('tiktoken');
const enc = get_encoding('o200k_base');

const ANSI = /\x1b\[[0-9;?]*[a-zA-Z]/g;
const OSC = /\x1b\][0-9;]*[^\x07\x1b]*(\x07|\x1b\\)/g;
const NOISE_LINES = [
  /^Attempt \d+ failed:.*$/gm,
  /^Loaded cached credentials\..*$/gm,
  /^warning: Codex.*$/gm,
  /^Reading additional input from stdin.*$/gm,
  /^OpenAI Codex v[\d\.]+.*$/gm,
  /^workdir:.*$/gm,
  /^model:.*$/gm,
  /^provider:.*$/gm,
  /^approval:.*$/gm,
  /^sandbox:.*$/gm,
  /^reasoning .*:.*$/gm,
  /^session id:.*$/gm,
  /^--------$/gm,
  /^user$/gm,
  /^codex$/gm,
  /^tokens used$/gm,
  /^This will modify your .* configuration:.*$/gm,
  /^ *\/home\/personal\/.*\.(json|md)$/gm,
  /^Backups will be saved.*$/gm,
  /^Preparing [A-Z].*\.\.\..*$/gm,
  /^Checking .*$/gm,
  /^Installing .*$/gm,
  /^Updating .*$/gm,
  /^Updated .*$/gm,
  /^  ✓ .*$/gm,
  /^Launching [A-Z].*\.\.\..*$/gm,
  /^Task started:.*$/gm,
  /^Error: exit status.*$/gm,
  /^\[\d+\]\s+(Done|Exit).*$/gm,
  /^\d[\d,]*$/gm,
  /^[╭╰├┤]+[─┈]+.*$/gm,
  /^│.*│$/gm,
  /^⠀.*$/gm,
  /^Resume this session with:$/gm,
  /^  hermes --resume.*$/gm,
  /^Session:\s+.*$/gm,
  /^Duration:\s+.*$/gm,
  /^Messages:\s+.*$/gm,
  /^Query:.*$/gm,
  /^Initializing agent.*$/gm,
  /^─{40,}$/gm,
  /^ (session agent|gateway|agent main|session main|connecting).*$/gm,
  /^ openclaw tui.*$/gm,
  /^🦞 OpenClaw.*$/gm,
  /^Changes\s+\+\d+.*$/gm,
  /^Tokens\s+↑.*$/gm,
];
const FENCE = /```[\s\S]*?```/g;

function clean(raw) {
  let t = raw.replace(ANSI,'').replace(OSC,'');
  for (const r of NOISE_LINES) t = t.replace(r,'');
  t = t.split('\n').map(l=>l.trimEnd()).filter(l=>l.trim()).join('\n').trim();
  const noFence = t.replace(FENCE,'').trim();
  if (noFence.length < 3 && t.length > 0) {
    return t.replace(/```[a-z]*\n?/g,'').replace(/```/g,'').trim();
  }
  return noFence;
}
function tok(s){ return s ? enc.encode(s).length : 0; }

if (require.main === module) {
  const fp = process.argv[2];
  if (!fp) { console.error('usage: tokenize.js <log>'); process.exit(1); }
  const raw = fs.readFileSync(fp,'utf8');
  const c = clean(raw);
  console.log(`${tok(c)}\t${fp}`);
  enc.free();
}
module.exports = { clean, tok };
