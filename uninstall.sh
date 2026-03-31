#!/usr/bin/env bash
set -euo pipefail

echo "Uninstalling arch-chart-example..."
helm uninstall arch-chart-example || echo "arch-chart-example not found, skipping."

echo "Done."
