import ipaddress
from pprint import pprint
import click

text1 = click.style('Hello World!', fg='green')
text2 = click.style('Some more text', bg='red', fg='white')
text3 = click.style('ATTENTION', bold=True)
print(text1, text2, text3)
with open("output.txt", "w") as f:
    f.write(f"{text1}\n{text2}\n{text3}\n")


click.echo(click.style('Hello World!', fg='green'))
click.echo(click.style('Some more text', bg='red', fg='white'))
click.echo(click.style('ATTENTION', bold=True))

click.secho('Hello World!', fg='green')
click.secho('Some more text', bg='red', fg='white')
click.secho('ATTENTION', bold=True)
