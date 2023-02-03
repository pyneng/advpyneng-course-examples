import click


def show_stats(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.secho("STATS", fg="green")
    ctx.exit()


@click.command()
@click.option("--pomodoros_to_run", "-p", default=5, show_default=True)
@click.option("--work_minutes", "-w", default=25, show_default=True)
@click.option("--short_break", "-s", default=5, show_default=True)
@click.option("--long_break", "-l", default=30, show_default=True)
@click.option("--set_size", "-s", default=4, show_default=True)
@click.option("--stats", callback=show_stats, is_eager=True, is_flag=True)
def cli(pomodoros_to_run, work_minutes, short_break, long_break, set_size, stats):
    print(f"{pomodoros_to_run=} {work_minutes=} {stats=}")


if __name__ == "__main__":
    cli()
