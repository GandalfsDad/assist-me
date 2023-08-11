from .OpenAI import make_simple_call as openai_make_simple_call, make_chat_call as openai_make_chat_call
from .PALM import make_simple_call as palm_make_simple_call, make_chat_call as palm_make_chat_call
from click.core import Context


def make_call(ctx: Context, **kwargs) -> None:
    command = ctx.command.name
    CALL_MAP[command](ctx, **kwargs)

def make_chat_call(ctx: Context, **kwargs) -> None:
    if ctx.obj['model']  in ['GPT3', 'GPT4']:
        return openai_make_chat_call(ctx, **kwargs)
    elif ctx.obj['model']  in ['PALM']:
        return palm_make_chat_call(ctx, **kwargs)
    raise NotImplementedError("Chat call not implemented")

def make_simple_call(ctx: Context, **kwargs) -> None:
    if ctx.obj['model']  in ['GPT3', 'GPT4']:
        return openai_make_simple_call(ctx, **kwargs)
    elif ctx.obj['model']  in ['PALM']:
        return palm_make_simple_call(ctx, **kwargs)
    raise NotImplementedError("Chat call not implemented")

CALL_MAP = {
    "chat": make_chat_call,
    "simple": make_simple_call,
}