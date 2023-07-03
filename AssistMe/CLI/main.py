import click
from ..Engine import make_call
from ..CLI import params as p
from AssistMe import __version__


@click.group()
@click.pass_context
def cli(ctx: click.core.Context, **kwargs) -> None:
    ctx.ensure_object(dict)

@cli.command('simple')
@click.pass_context
@p._model
@p._name
@p._input
@p._system
def simple(ctx: click.core.Context, **kwargs) -> None:
    ctx = p.parse_params(ctx, **kwargs)
    make_call(ctx)

@cli.command('chat')
@click.pass_context
@p._model
@p._name
@p._system
def chat(ctx: click.core.Context, **kwargs) -> None:
    ctx = p.parse_params(ctx, **kwargs)
    make_call(ctx)

@cli.command('version')
@click.pass_context
def version(ctx: click.core.Context, **kwargs) -> None:
    click.echo(f"AssistMe version: {__version__}")

if __name__ == '__main__':
    cli(obj={})