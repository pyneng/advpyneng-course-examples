import click


@click.command()
@click.option("--day", "-d", is_flag=True)
@click.option("--week", "-w", is_flag=True)
@click.option("--month", "-m", is_flag=True)
def pomodoro_stats(day, week, month):
    print("STATS")


if __name__ == "__main__":
    pomodoro_stats()

