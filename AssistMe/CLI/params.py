import click

_name = click.option('--name', '-n', 
                        default='Assistant', 
                        help='Name of Assistant')

_model = click.option('--model','-m', 
                        default='GPT3',
                        type=click.Choice(['GPT3', 'GPT4'], case_sensitive=False),
                        help='Model to use for generating text')

_input = click.option('--input', '-i',
                        prompt = "You", 
                        help='Input text')

def parse_params(ctx: click.core.Context, **kwargs):
    for key, value in kwargs.items():
        ctx.obj[key] = value
    return ctx
