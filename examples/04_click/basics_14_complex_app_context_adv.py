from pprint import pprint
import click
from rich import inspect


@click.group()
@click.option("--db-filename", "-d", default="dhcp.db", help="db filename")
@click.pass_context
def dhcp_db(context, db_filename):
    print(f"GROUP {context=} {db_filename=}")
    # inspect(context)
    context.obj = {"db_filename": db_filename}


@dhcp_db.command()
@click.option("--db-schema", "-s", help="db schema filename")
@click.pass_context
def create(context, db_schema):
    """
    create DB
    """
    print(f"CREATE {context=} {db_schema=}")


@dhcp_db.command()
@click.argument("filenames", nargs=-1, required=True)
@click.pass_context
def add(context, filenames):
    """
    add data to db from FILENAMES
    """
    print(f"ADD {context=} {filenames=}")


@dhcp_db.command()
@click.argument("value", type=(click.Choice(["mac", "ip", "vlan"]), str))
@click.pass_context
def get(context, value):
    """
    get data from db
    """
    # inspect(context)
    print(f"GET {context=} {value=}")


if __name__ == "__main__":
    dhcp_db()
