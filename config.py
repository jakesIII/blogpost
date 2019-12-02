import os

class Config():

    QUOTES_BASE_URL=os.environ.get('QUOTES_BASE_URL')
    

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG=True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI_DEV")

config_options={
'productions':ProdConfig,
'development':DevConfig
}
