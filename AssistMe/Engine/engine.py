from .OpenAI import make_simple_call as openai_make_simple_call, make_chat_call as openai_make_chat_call


def make_call(ctx, **kwargs):
    command = ctx.command.name
    CALL_MAP[command](ctx, **kwargs)

def make_chat_call(ctx, **kwargs):
    if ctx.obj['model']  in ['GPT3', 'GPT4']:
        return openai_make_chat_call(ctx, **kwargs)
    raise NotImplementedError("Chat call not implemented")

def make_simple_call(ctx, **kwargs):
    if ctx.obj['model']  in ['GPT3', 'GPT4']:
        return openai_make_simple_call(ctx, **kwargs)
    raise NotImplementedError("Chat call not implemented")

CALL_MAP = {
    "chat": make_chat_call,
    "simple": make_simple_call,
}