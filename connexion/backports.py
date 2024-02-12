import json
import typing as t

from flask.json.provider import _default


class JSONEncoder(json.JSONEncoder):
    """The default JSON encoder. Handles extra types compared to the
    built-in :class:`json.JSONEncoder`.

    -   :class:`datetime.datetime` and :class:`datetime.date` are
        serialized to :rfc:`822` strings. This is the same as the HTTP
        date format.
    -   :class:`decimal.Decimal` is serialized to a string.
    -   :class:`uuid.UUID` is serialized to a string.
    -   :class:`dataclasses.dataclass` is passed to
        :func:`dataclasses.asdict`.
    -   :class:`~markupsafe.Markup` (or any object with a ``__html__``
        method) will call the ``__html__`` method to get a string.

    Assign a subclass of this to :attr:`flask.Flask.json_encoder` or
    :attr:`flask.Blueprint.json_encoder` to override the default.

    .. deprecated:: 2.2
        Will be removed in Flask 2.3. Use ``app.json`` instead.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def default(self, o: t.Any) -> t.Any:
        """Convert ``o`` to a JSON serializable type. See
        :meth:`json.JSONEncoder.default`. Python does not support
        overriding how basic types like ``str`` or ``list`` are
        serialized, they are handled before this method.
        """
        return _default(o)
