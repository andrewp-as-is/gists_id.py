#!/usr/bin/env python
"""print gists id"""
import click
import github
import os

MODULE_NAME = "gists_id"
USAGE = 'python -m %s' % MODULE_NAME
PROG_NAME = 'python -m %s ' % USAGE


@click.command()
def _cli():
    g = github.Github(os.environ["GITHUB_TOKEN"])
    for gist in g.get_user().get_gists():
        print(gist.id)


if __name__ == "__main__":
    _cli()
