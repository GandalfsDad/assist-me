from .chat import Chat

def make_simple_call(ctx, **kwargs) -> None:
    model = ctx.obj['model']
    if model == 'GPT3':
        _model = 'gpt-3.5-turbo'
    elif model == 'GPT4':
        _model = 'gpt-4'
    else:
        raise NotImplementedError(f"Model [{model}] is not implemented")

    chat = Chat(model=_model)
    response = chat.generate_response(ctx.obj['input'])

    print(f"Response: {response}")
    
def make_chat_call(ctx, **kwargs) -> None:
    model = ctx.obj['model']
    if model == 'GPT3':
        _model = 'gpt-3.5-turbo'
    elif model == 'GPT4':
        _model = 'gpt-4'
    else:
        raise NotImplementedError(f"Model [{model}] is not implemented")

    chat = Chat(model=_model)

    chat.interactive()