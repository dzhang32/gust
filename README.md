# gust

What's the main goal of this package?

## Installation

I recommend using [uv](https://docs.astral.sh/uv/) to manage the python version, virtual environment and `gust` installation:

```bash
uv venv --python 3.13
source .venv/bin/activate
uv pip install gust
```

## Additional setup

### Code coverage

- Add a "CODECOV_TOKEN" secret (obtained from [here](https://app.codecov.io/gh/dzhang32/test_python_package/)) to your repo via `Settings` -> `Secrets and variables` -> `Actions`. 




### Deploying to PyPI

- Go to your [PyPi publishing settings](https://pypi.org/manage/account/publishing/) and fill in the following details:

    - **PyPI Project Name:** gust
    - **Owner:** dzhang32
    - **Repository name:** gust
    - **Workflow name:** test_deploy.yml
    - **Environment name:** (leave blank)

