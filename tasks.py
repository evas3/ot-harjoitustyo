from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/recipes.py", pty=True)

@task
def test(ctx):
    ctx.run("cd src && python3 -m tests.resepti_test", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
