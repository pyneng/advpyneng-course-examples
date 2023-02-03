import click
from rich import inspect


@click.group()
@click.option("--db-filename", "-d", default="dhcp.db", help="db filename")
@click.pass_context
def dhcp_db(context, db_filename):
    print("GROUP")
    # inspect(context)
    context.obj = {"db_filename": db_filename}


@dhcp_db.command()
@click.option("--db-schema", "-s", help="db schema filename")
@click.pass_context
def create(context, db_schema):
    """
    create DB
    """
    db_filename = context.obj.get("db_filename")
    print(f"CREATE {db_schema=} {db_filename=}")


@dhcp_db.command()
@click.argument("filenames", nargs=-1, required=True)
@click.pass_context
def add(context, filenames):
    """
    add data to db from FILENAMES
    """
    db_filename = context.obj.get("db_filename")
    print(f"ADD {filenames=} {db_filename=}")


@dhcp_db.command()
@click.option("--key", "-k", type=click.Choice(["mac", "ip", "vlan"]))
@click.option("--value", "-v", help="value of key")
@click.pass_context
def get(context, key, value):
    """
    get data from db
    """
    db_filename = context.obj.get("db_filename")
    print(f"GET {key=} {value=} {db_filename=}")
    # inspect(context)


if __name__ == "__main__":
    dhcp_db()
