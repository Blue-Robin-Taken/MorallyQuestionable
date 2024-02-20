# About
This is a project for the [QubitX Hacks by YCW](https://qubitx.devpost.com/) hackathon.
It's a project that questions people's moralities. This is not to start quarrels or to be political. 
This is just a study to see how people would react/respond to certain topics of morality.

# What we hope to do
We're hoping to see that people think similarly on topics related to morality.
We want to bring people together instead of pulling them apart.

# How we're going to achieve this
We're going to use a system of reputation similar to Stack Overflow.
People can ask their own questions related to morality and other people can 
answer them. People with higher reputation (like in Stack Overflow) can moderate the site.
This will help avoid people asking things related to politics (which tend to bring people apart).
It will also let the community choose better outcomes for the site itself.

# How to run this project

## For Flask
Run the following for Flask:
```bash
flask --app main.py --debug run
```
Remove --debug if in production.

## Adding npm packages

```bash
npm install
```

Tailwind (might already be installed though):
```bash
npm install -D tailwindcss
```

# Contributing to this project

## For people new to GitHub
You'll need to learn how to program in HTML and Flask. For contributions, you'll need
to learn how to use GitHub.

See the following tutorials:
- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
- https://www.youtube.com/watch?v=jRLGobWwA3Y

## CSS
For CSS, run the tailwind compile command:

```bash
npx tailwindcss -i ./static/style.css -o ./static/output.css --watch
```

Every time you save the style.css file in the static dir,
it should save your changes to output.css. This includes tailwind changes.