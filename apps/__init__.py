# import os
# from dotenv import load_dotenv
# print("Loading environment variables")
# load_dotenv(override=False)
#
# def validate_required_env():
#     if os.environ.get('ENVIRONMENT') is None or \
#             os.environ.get('ENVIRONMENT') not in ['LOCAL', 'DEV', 'STAGING', 'PROD']:
#         raise ValueError('Incorrect ENVIRONMENT = {}'.format(os.environ.get('ENVIRONMENT')))
#
#     if os.environ.get('REGION') is None:
#         raise ValueError('Incorrect REGION = {}'.format(os.environ.get('REGION')))
#
# validate_required_env()
#
# from app.config import Config
#
# import logging
# from logging import config as logging_config
#
# def set_logging():
#     from app_logging import app_logging_config
#     global logger
#
#     app_logging_config['formatters']['night_watch']['format']['hostname'] = \
#         app_logging_config['handlers']['fluent_async_handler']['tag']
#
#     logging_config.dictConfig(app_logging_config)
#
#     logger = logging.getLogger(Config.APP_NAME)
#     logger.info('Logger ready')
#     return logger
#
# logger = set_logging()
#
#
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
#
#
# # Must be same as APP_INSTANCE_NAME
# identity_app = Flask(Config.APP_NAME)
# identity_app.config['CORS_HEADERS'] = 'Content-Type'
# cors = CORS(identity_app)
# identity_app.config.from_object(Config)
# db = SQLAlchemy(identity_app)
#
# from app.api import blue_print as api_bp
#
# identity_app.register_blueprint(api_bp)
#
#
# if __name__ == 'app':
#     logger.info(f'Application ready in {Config.ENVIRONMENT} mode')
