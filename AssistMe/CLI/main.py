import click
from ..Engine import make_call

@click.group()
@click.option('--model','-m', default='GPT3', 
              type=click.Choice(['GPT3', 'GPT4'], case_sensitive=False),
              help='Model to use for generating text')
@click.pass_context
def cli(ctx, model):
    ctx.ensure_object(dict)

    ctx.obj['model'] = model
    pass

@cli.command('simple')
@click.pass_context
@click.option('--input', '-i',prompt = "Input", help='Input text')
def simple(ctx, input):
    ctx.obj['input'] = input
    make_call(ctx)

@cli.command('chat')
@click.pass_context
def chat(ctx):
    make_call(ctx)

if __name__ == '__main__':
    cli(obj={})