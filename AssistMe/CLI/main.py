import click
from ..Engine import make_call
from ..CLI import params as p
from .profile import output_profile, output_profiles
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
@p._profile
@p._max_tokens
@p._temperature
def simple(ctx: click.core.Context, **kwargs) -> None:
    ctx = p.parse_params(ctx, **kwargs)
    make_call(ctx)

@cli.command('chat')
@click.pass_context
@p._model
@p._name
@p._system
@p._profile
@p._max_tokens
@p._temperature
def chat(ctx: click.core.Context, **kwargs) -> None:
    ctx = p.parse_params(ctx, **kwargs)
    make_call(ctx)

@cli.command('save-profile')
@click.pass_context
@p._profile
@p._system
def save_profile(ctx: click.core.Context, **kwargs) -> None:
    ctx = p.parse_params(ctx, **kwargs)
    click.echo("Profile Saved")

@cli.command('show-profile')
@p._profile
def show_profile(**kwargs) -> None:
    output_profile(kwargs['profile'])
    
@cli.command('show-profiles')
def show_profiles(**kwargs) -> None:
    output_profiles()
    
@cli.command('version')
def version( **kwargs) -> None:
    click.echo(f"AssistMe version: {__version__}")

if __name__ == '__main__':
    cli(obj={})