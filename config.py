class Config(object):
	#Common configs
	DEBUG=False

class DevelopmentConfig(Config):
	#Dev configs
    DEBUG=True
    SQLALCHEMY_ECHO=True

class ProductionConfig(Config):
    DEBUG=False

app_config={
	'development': DevelopmentConfig,
	'production': ProductionConfig
}