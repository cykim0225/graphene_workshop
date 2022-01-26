# graphene_workshop

A graphene-python workshop

You should have this installed prior to the workshop:
* Python3
* pip

## Setup
1. Create the project directory
2. Clone the repo
3. Go to the folder
5. Run `./bin/setup` which will install Poetry (package manager), install project dependencies using poetry, and set up pre-commit hooks locally

## Run
1. `cd graphene_workshop && poetry shell`
2. Run the app: `python runserver.py`

```
Output:
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) <------ Open the link on your browser
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 768-535-817
```

3. Navigate to `http://127.0.0.1:5000/graphql` to access the GraphiQL playground.
4. Type hello in the GraphiQL
```
{
  hello
}
```
