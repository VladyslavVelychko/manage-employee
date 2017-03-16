class Config(object):
	#Common configs
	DEBUG=False
	SQLALCHEMY_TRACK_MODIFICATIONS=True

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