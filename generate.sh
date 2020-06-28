#!/bin/bash
export RSE_HOST=https://rseng.github.io
export RSE_URL_PREFIX=/software/
export RSE_CONFIG_FILE=rse.ini
rse export --type static-web docs/
