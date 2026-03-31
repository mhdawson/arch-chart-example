#!/usr/bin/env python3
"""
Simple llama-stack chat completion test script.

Usage:
    python test_chat.py --endpoint http://localhost:8321
    python test_chat.py --endpoint http://localhost:8321 --message "Explain quantum computing"

Setup:
    pip install llama-stack-client
"""

import argparse
import sys

try:
    from llama_stack_client import LlamaStackClient
except ImportError:
    print("Error: llama-stack-client not installed. Run: pip install llama-stack-client")
    sys.exit(1)


DEFAULT_MODEL = "llama-3-2-3b-instruct/meta-llama/Llama-3.2-3B-Instruct"


def main():
    parser = argparse.ArgumentParser(description="Test llama-stack chat completion")
    parser.add_argument(
        "--endpoint",
        required=True,
        help="Llama stack base URL, e.g. http://localhost:8321",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Model ID to use (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--message",
        default="What is the capital of France? Answer in one sentence.",
        help="Message to send to the model",
    )
    args = parser.parse_args()

    client = LlamaStackClient(base_url=args.endpoint)

    print(f"Endpoint : {args.endpoint}")
    print(f"Model    : {args.model}")
    print(f"Message  : {args.message}")
    print()

    response = client.chat.completions.create(
        model=args.model,
        messages=[{"role": "user", "content": args.message}],
    )

    print("Response:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
