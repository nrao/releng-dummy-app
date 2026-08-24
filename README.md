# Release Engineering Dummy App

A minimal app for testing and demoing GitOps processes.

## App
The app runs a simple webserver and has two endpoints:

- `/healthz` returns a json object containing the app version as a string
- `/` displays a very simple web page that also has the app version, as well as content that is set via environment variables

### Environment Variables

The following environment variables can be set in the built container image, or locally in a `.env` file:

| Variable | Default | Valid Values | Description |
| --- | --- | --- | --- |
| `SAMPLE_VAR` | `"UNSET"` | Any string | A text value that is displayed on the webpage |
| `COLOR` | `none` | `none`, `yellow`, `orange`, `red`, `magenta`, `violet`, `blue`, `cyan`, `green` | Sets the background color of the webpage. Valid values are the (non-`base`) [Solarized](https://ethanschoonover.com/solarized/) color names (e.g. `blue`, `red`, `cyan`, etc.) |
| `CONTEXT_PATH` | `/` | A URL subpath | The subpath the app is deployed at |

### TODOS
- [ ] smoke/integration tests

# Development

## Install development dependencies
```bash
pip install -e .
```

## Run app in dev mode
```bash
./runDev.sh
```

## Build container
```bash
docker build -t nrao/releng/dummy_app:local .
```

## Run the built container
```bash
docker run --rm \
    -p 8000:5000 \
    --name dummyapp \
    nrao/releng/dummy_app:local
```

## Troubleshooting

### Some docker actions fail when run with `act`
If the error mentions something about 'Bad Credentials' or a bad token, you probably need to setup a `GITHUB_TOKEN` and [pass it to `act`](https://nektosact.com/usage/index.html#github_token)

# Testing

## Install testing dependencies
```bash
pip install -e . --group test
```

## Run unit tests
```bash
pytest tests/unit/
```

## Run smoke tests
> Note: Requires the app to be running - by default the smoke tests will work against the dev server run via `./runDev.sh`

```bash
pytest tests/smoke/
```

## Build testing container
```bash
docker build -t nrao/releng/dummy_app/tests:local -f tester.dockerfile .
```

## Run testing container against a running dummy-app container
1. Create a testing network in docker
```bash
docker network create dummy-app-test
```

2. Run the dummy-app container in the test network
```bash
docker run -d --rm \
    -p 5000:5000 \
    --name dummy-app \
    --network dummy-app-test \
    nrao/releng/dummy_app:local
```

3. Run the test container (by default, runs the smoke tests)
```bash
docker run --rm \
    --network dummy-app-test \
    nrao/releng/dummy_app/tests:local
```
