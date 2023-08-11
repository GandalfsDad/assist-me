from .chat import Chat
from click.core import Context

def make_simple_call(ctx: Context, **kwargs) -> None:
    chat = setup_chat(ctx)
    chat.generate_response(ctx.obj['input'])
    pass

    
def make_chat_call(ctx: Context, **kwargs) -> None:
    chat = setup_chat(ctx)
    chat.interactive()
    pass

def setup_chat(ctx: Context) -> Chat:
    model = ctx.obj['model']
    if model == 'PALM':
         _model = 'models/chat-bison-001'
    else:
        raise NotImplementedError(f"Model [{model}] is not implemented")


    chat = Chat(model=_model, name=ctx.obj['name'], context=ctx.obj['system'], temperature=ctx.obj['temperature'])

    return chat