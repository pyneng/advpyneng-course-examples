import click
from rich import inspect


@click.group()
def dhcp_db():
    print("GROUP")


@dhcp_db.command()
@click.option("--db-schema", "-s", help="db schema filename")
@click.argument("db-filename")
def create(db_schema, db_filename):
    """
    create DB
    """
    print(f"CREATE {db_schema=} {db_filename=}")


@dhcp_db.command()
@click.argument("db-filename")
@click.argument("filenames", nargs=-1, required=True)
def add(filenames, db_filename):
    """
    add data to db from FILENAMES
    """
    print(f"ADD {filenames=} {db_filename=}")


@dhcp_db.command()
@click.argument("db-filename")
@click.option("--key", "-k", type=click.Choice(["mac", "ip", "vlan"]))
@click.option("--value", "-v", help="value of key")
def get(key, value, db_filename):
    """
    get data from db
    """
    print(f"GET {key=} {value=} {db_filename=}")


if __name__ == "__main__":
    dhcp_db()
