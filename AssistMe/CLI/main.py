import click

@click.group()
@click.option('--model','-m', default='gpt3', 
              type=click.Choice(['GPT3', 'GPT4'], case_sensitive=False),
              help='Model to use for generating text')
@click.pass_context
def cli(ctx, model):
    ctx.ensure_object(dict)

    ctx.obj['model'] = model
    pass

@cli.command('simple')
@click.pass_context
def simple(ctx):
    click.echo(f"model: {ctx.obj['model']}")

@cli.command('chat')
@click.pass_context
def chat(ctx):
    click.echo(f"model: {ctx.obj['model']}")

if __name__ == '__main__':
    cli(obj={})