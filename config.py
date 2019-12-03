import os

class Config():

    SECRET_KEY=os.environ.get('SECRET_KEY')
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):

    pass

class DevConfig(Config):
    
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Jacques@localhost/blogpost'
    DEBUG=True


config_options={
'productions':ProdConfig,
'development':DevConfig
}
