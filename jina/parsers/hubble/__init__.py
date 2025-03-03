from jina.parsers.base import set_base_parser
from jina.parsers.helper import _chf


def mixin_hub_usage_parser(parser):
    """Add the arguments for hub pull to the parser
    :param parser: the parser configure
    """
    parser.add_argument(
        '--no-usage',
        action='store_true',
        default=False,
        help='If set, Hub executor usage will not be printed.',
    )


def set_hub_push_parser(parser=None):
    """Set the parser for the hub push
    :param parser: an optional existing parser to build upon
    :return: the parser
    """
    if not parser:
        parser = set_base_parser()

    from jina.parsers.hubble.push import mixin_hub_push_parser

    mixin_hub_usage_parser(parser)
    mixin_hub_push_parser(parser)
    return parser


def set_hub_pull_parser(parser=None):
    """Set the parser for the hub pull
    :param parser: an optional existing parser to build upon
    :return: the parser
    """
    if not parser:
        parser = set_base_parser()

    from jina.parsers.hubble.pull import mixin_hub_pull_parser

    mixin_hub_usage_parser(parser)
    mixin_hub_pull_parser(parser)
    return parser


def set_hub_new_parser(parser=None):
    """Set the parser for the hub new
    :param parser: an optional existing parser to build upon
    :return: the parser
    """
    if not parser:
        parser = set_base_parser()

    from jina.parsers.hubble.new import mixin_hub_new_parser

    mixin_hub_new_parser(parser)
    return parser


def set_hub_status_parser(parser=None):
    """Set the parser for the hub status
    :param parser: an optional existing parser to build upon
    :return: the parser
    """
    if not parser:
        parser = set_base_parser()

    from jina.parsers.hubble.status import mixin_hub_status_parser

    mixin_hub_status_parser(parser)
    return parser


def set_hub_parser(parser=None):
    """Set the parser for the hub
    :param parser: the parser configure

    :return: the parser
    """
    if not parser:
        parser = set_base_parser()

    spp = parser.add_subparsers(
        dest='hub',
        description='use `%(prog)-8s [sub-command] --help` '
        'to get detailed information about each sub-command',
        required=True,
    )

    set_hub_new_parser(
        spp.add_parser(
            'new',
            help='create a new executor using the template',
            description='Create a new executor using the template',
            formatter_class=_chf,
        )
    )

    set_hub_push_parser(
        spp.add_parser(
            'push',
            help='push an executor package to Jina hub',
            description='Push an executor package to Jina hub',
            formatter_class=_chf,
        )
    )

    set_hub_pull_parser(
        spp.add_parser(
            'pull',
            help='download an executor image/package from Jina hub',
            description='Download an executor image/package from Jina hub',
            formatter_class=_chf,
        )
    )

    set_hub_status_parser(
        spp.add_parser(
            'status',
            help='query an executor building status of of a pushed Executor from Jina hub',
            description='Query an executor building status of of a pushed Executor from Jina hub',
            formatter_class=_chf,
        )
    )

    return parser
