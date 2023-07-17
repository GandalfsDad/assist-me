import click
from ..Engine.OpenAI import DEFAULT_SYSTEM_PROMPT, DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE
from .profile import load_profile, save_profile

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

_system = click.option('--system', '-s',
                        default=DEFAULT_SYSTEM_PROMPT,
                        help='System prompt')

_profile = click.option('--profile', '-p',
                        default='base',
                        help='Profile Name')

_max_tokens = click.option('--max-tokens',
                        default=DEFAULT_MAX_TOKENS,
                        help='Max tokens for OpenAI Model')

_temperature = click.option('--temperature',
                        default=DEFAULT_TEMPERATURE,
                        help='Temperature for OpenAI Model')

def parse_params(ctx: click.core.Context, **kwargs):

    if kwargs['profile'].lower() != 'base':
        if kwargs['system'] == DEFAULT_SYSTEM_PROMPT:
            try:
                kwargs['system'] = load_profile(kwargs['profile'].lower())
            except FileNotFoundError:
                click.echo("Profile not found please create profile.")
                profile_prompt = click.prompt("System Prompt")
                save_profile(kwargs['profile'].lower(), profile_prompt)
        else:
            save_profile(kwargs['profile'].lower(), kwargs['system'])

    for key, value in kwargs.items():
        ctx.obj[key] = value
    return ctx
