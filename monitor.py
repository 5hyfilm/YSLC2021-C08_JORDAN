import logging
from opencensus.ext.azure.log_exporter import AzureEventHandler

logger = logging.getLogger(__name__)
logger.addHandler(AzureEventHandler(connection_string='InstrumentationKey=dbbde929-464a-41c7-b963-d299472157c4'))
logger.setLevel(logging.INFO)
logger.info('Hello, World!')