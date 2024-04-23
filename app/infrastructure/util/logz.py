import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install

class LoggerAdapter(logging.LoggerAdapter):
    def __init__(self, prefix, logger):
        super(LoggerAdapter, self).__init__(logger, {})
        self.prefix = prefix

    def process(self, msg, kwargs):
        return '[%s] %s' % (self.prefix, msg), kwargs

install()
def create_logger(prefix="[bold cyan]CEFET-IN[/bold cyan]"):
    rich_handler = RichHandler(rich_tracebacks=True, markup=True)
    logging.basicConfig(level='INFO', format='%(message)s',
                        datefmt="[%Y/%m/%d %H:%M;%S]",
                        handlers=[rich_handler])
    logger = logging.getLogger('rich')
    logger = LoggerAdapter(prefix, logger)
    return logger
