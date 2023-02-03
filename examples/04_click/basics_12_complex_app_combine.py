import click
from basics_12_complex_app_combine_stats import pomodoro_stats


@click.group()
def pomodoro():
    pass


@pomodoro.command()
@click.option("--pomodoros_to_run", "-r", default=5, show_default=True, type=int)
@click.option("--work_minutes", "-w", default=25, show_default=True, type=int)
@click.option("--short_break", "-s", default=5, show_default=True, type=int)
@click.option("--long_break", "-l", default=30, show_default=True, type=int)
@click.option("--set_size", "-p", default=4, show_default=True, type=int)
def timer(pomodoros_to_run, work_minutes, short_break, long_break, set_size):
    pass

pomodoro.add_command(pomodoro_stats, name="stats")

if __name__ == "__main__":
    pomodoro()

