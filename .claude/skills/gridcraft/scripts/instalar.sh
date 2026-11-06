#!/usr/bin/env bash
# Garante que photocraft-cli está disponível. Ordem: o do PATH; senão o binário da release oficial
# (Linux, conferido pelo SHA256SUMS.txt da própria release, ~1 s); senão compila com cargo (Rust 1.95+).
set -euo pipefail
APP=gridcraft

if command -v $APP-cli >/dev/null 2>&1; then
  $APP-cli --version
  exit 0
fi

DEST="${HOME}/.local/share/craft"
BIN="${HOME}/.local/bin"
case "$(uname -s)-$(uname -m)" in
  Linux-x86_64) ARQ=x86_64 ;;
  Linux-aarch64|Linux-arm64) ARQ=aarch64 ;;
  *) ARQ="" ;;
esac

if [ -n "$ARQ" ]; then
  URL="https://github.com/storytold/$APP/releases/latest/download"
  TMP="$(mktemp -d)"
  trap 'rm -rf "$TMP"' EXIT
  if curl -sfL --retry 3 -o "$TMP/SHA256SUMS.txt" "$URL/SHA256SUMS.txt"; then
    NOME="$(awk -v a="$APP" -v q="$ARQ" '$2 ~ "^"a"-[0-9.]+-linux-"q"\\.tar\\.gz$" {print $2; exit}' "$TMP/SHA256SUMS.txt")"
    if [ -n "$NOME" ] && curl -sfL --retry 3 -o "$TMP/$NOME" "$URL/$NOME" \
       && (cd "$TMP" && grep " $NOME\$" SHA256SUMS.txt | sha256sum -c --quiet); then
      mkdir -p "$DEST" "$BIN"
      tar -xzf "$TMP/$NOME" -C "$DEST"
      ln -sf "$DEST/${NOME%.tar.gz}/bin/$APP-cli" "$BIN/$APP-cli"
      export PATH="$BIN:$PATH"
      $APP-cli --version
      echo "instalado em $BIN/$APP-cli (adicione $BIN ao PATH se preciso)"
      exit 0
    fi
  fi
  echo "release pronta indisponível; tentando compilar" >&2
fi

if ! command -v cargo >/dev/null 2>&1; then
  echo "cargo não encontrado: instale o Rust (https://rustup.rs) ou baixe a CLI em" >&2
  echo "https://github.com/storytold/$APP/releases/latest" >&2
  exit 1
fi

cargo install --git https://github.com/storytold/$APP --locked $APP-cli
export PATH="${CARGO_HOME:-$HOME/.cargo}/bin:$PATH"
$APP-cli --version
