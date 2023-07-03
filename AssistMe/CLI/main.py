import click
from ..Engine import make_call

@click.group()
@click.option('--model','-m', default='GPT3', 
              type=click.Choice(['GPT3', 'GPT4'], case_sensitive=False),
              help='Model to use for generating text')
@click.option('--name', '-n', default='Assistant')
@click.pass_context
def cli(ctx: click.core.Context, model: str, name: str) -> None:
    ctx.ensure_object(dict)

    ctx.obj['model'] = model
    ctx.obj['name'] = name

@cli.command('simple')
@click.pass_context
@click.option('--input', '-i',prompt = "You", help='Input text')
def simple(ctx: click.core.Context, input: str) -> None:
    ctx.obj['input'] = input
    make_call(ctx)

@cli.command('chat')
@click.pass_context
def chat(ctx: click.core.Context) -> None:
    make_call(ctx)

if __name__ == '__main__':
    cli(obj={})