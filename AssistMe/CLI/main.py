import click
from ..Engine import make_call
from ..CLI import params as p

@click.group()
@click.pass_context
def cli(ctx: click.core.Context, **kwargs) -> None:
    ctx.ensure_object(dict)

@cli.command('simple')
@click.pass_context
@p._model
@p._name
@p._input
def simple(ctx: click.core.Context, **kwargs) -> None:
    ctx = p.parse_params(ctx, **kwargs)
    make_call(ctx)

@cli.command('chat')
@click.pass_context
@p._model
@p._name
def chat(ctx: click.core.Context, **kwargs) -> None:
    ctx = p.parse_params(ctx, **kwargs)
    make_call(ctx)

if __name__ == '__main__':
    cli(obj={})