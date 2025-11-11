#!/bin/bash
# Convenience script to run benchmarks for specific scenarios

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=====================================${NC}"
echo -e "${BLUE}  Memory Leak Benchmark Runner${NC}"
echo -e "${BLUE}=====================================${NC}"
echo ""

# Show usage
show_usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --quick              Run quick test (balanced config, small scale)"
    echo "  --scenario <name>    Run specific scenario (sqlalchemy1x, sqlalchemy2x, etc.)"
    echo "  --all                Run all scenarios with all configs"
    echo "  --config <name>      Run specific CRUD config (balanced, read_heavy, etc.)"
    echo "  --scale <size>       Run specific scale (small=10k, medium=100k, large=1M)"
    echo "  --help               Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 --quick"
    echo "  $0 --scenario sqlalchemy1x --config balanced --scale small"
    echo "  $0 --all"
    echo ""
}

# Parse arguments
if [ $# -eq 0 ]; then
    echo -e "${YELLOW}No arguments provided. Running quick test...${NC}"
    echo ""
    python3 run_benchmarks.py --quick
    exit 0
fi

if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    show_usage
    exit 0
fi

# Run the Python script with passed arguments
echo -e "${GREEN}Starting benchmarks...${NC}"
echo ""

python3 run_benchmarks.py "$@"

echo ""
echo -e "${GREEN}Benchmarks completed!${NC}"
echo ""
