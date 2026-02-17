#!/bin/bash
set -e  # Stop on first failure

# echo "Running JSON Schema Tests..."
# promptfoo eval -c configs/deterministicEvalJson.yaml

# echo "Running Refusal Tests..."
# promptfoo eval -c configs/deterministicEvalRefusal.yaml

echo "Running Similarity Tests..."
promptfoo eval -c configs/modelAssistedEvalSimilarity.yaml

echo "All tests complete!"