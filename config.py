

class Config:
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adnan:New Password@localhost/pitcher'
    SECRET_KEY = '61cc731520a271e4fc6d3926'

    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
