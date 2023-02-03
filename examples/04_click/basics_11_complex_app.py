import click


@click.group()
def pomodoro_cli():
    pass


@pomodoro_cli.command()
@click.option("--day", "-d", is_flag=True)
@click.option("--week", "-w", is_flag=True)
@click.option("--month", "-m", is_flag=True)
def stats(day, week, month):
    print(f"STATS {day=} {week=} {month=}")


@pomodoro_cli.command()
@click.option("--pomodoros_to_run", "-p", default=5, show_default=True)
@click.option("--work_minutes", "-w", default=25, show_default=True)
@click.option("--short_break", "-s", default=5, show_default=True)
@click.option("--long_break", "-l", default=30, show_default=True)
@click.option("--set_size", "-s", default=4, show_default=True)
def timer(pomodoros_to_run, work_minutes, short_break, long_break, set_size):
    print(f"WORK {pomodoros_to_run=} {work_minutes=}")


if __name__ == "__main__":
    pomodoro_cli()
