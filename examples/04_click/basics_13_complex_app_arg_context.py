import click
from rich import inspect


@click.group()
@click.argument("db-filename")
@click.pass_context
def dhcp_db(context, db_filename):
    print("GROUP")


@dhcp_db.command()
@click.option("--db-schema", "-s", help="db schema filename")
@click.pass_context
def create(context, db_schema):
    """
    create DB
    """
    print(f"CREATE {db_schema=} {context=}")


@dhcp_db.command()
@click.argument("filenames", nargs=-1, required=True)
@click.pass_context
def add(context, filenames):
    """
    add data to db from FILENAMES
    """
    print(f"ADD {filenames=} {context=}")


@dhcp_db.command()
@click.option("--key", "-k", type=click.Choice(["mac", "ip", "vlan"]))
@click.option("--value", "-v", help="value of key")
@click.pass_context
def get(context, key, value):
    """
    get data from db
    """
    print(f"GET {key=} {value=} {context=}")


if __name__ == "__main__":
    dhcp_db()
