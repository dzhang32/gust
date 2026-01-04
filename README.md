# gust

`gust` generates a summary of the weekly offshore wind news using the Anthropic API.

## Installation

I recommend using [uv](https://docs.astral.sh/uv/) to manage the Python version, virtual environment and `gust` installation:

```
git clone git@github.com:dzhang32/gust.git
cd gust
uv venv --python 3.13
source .venv/bin/activate
uv pip install .
```

## Usage

`gust` retrieves and sends a summary of the latest offshore wind news as an email to a provided recipient. `gust` is designed to be used as a CLI tool, with a single command:

```
> gust --help
Usage: gust [OPTIONS]

  Gust - Generate and send daily offshore wind industry reports.

Options:
  --model TEXT             Model to use for generation.
  --api-key TEXT           Claude API key.  [required]
  --sender TEXT            Sender email address.  [required]
  --sender-password TEXT   Sender email password.  [required]
  --recipient TEXT         Recipient email address.  [required]
  --help                   Show this message and exit.
```

The below arguments can also be set via environment variables:

| Argument             | Environment Variable   |
|--------------------|------------------------|
| `--api-key`        | `CLAUDE_API_KEY`       |
| `--sender`         | `GUST_SENDER`          |
| `--sender-password`| `GUST_SENDER_PASSWORD` |
| `--recipient`      | `GUST_RECIPIENT`       |
