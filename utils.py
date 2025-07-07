async def update(form, object):
    for col, val in dict(form).items():
        setattr(object, col, val)
    return object
