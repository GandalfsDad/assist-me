from .chat import Chat
from click.core import Context

def make_simple_call(ctx: Context, **kwargs) -> None:
    chat = setup_chat(ctx)
    chat.generate_response(ctx.obj['input'])

    
def make_chat_call(ctx: Context, **kwargs) -> None:
    chat = setup_chat(ctx)
    chat.interactive()

def setup_chat(ctx: Context) -> Chat:
    model = ctx.obj['model']
    if model == 'GPT3':
        _model = 'gpt-3.5-turbo'
    elif model == 'GPT4':
        _model = 'gpt-4'
    else:
        raise NotImplementedError(f"Model [{model}] is not implemented")


    chat = Chat(model=_model, name=ctx.obj['name'], system_prompt=ctx.obj['system'])

    return chat
