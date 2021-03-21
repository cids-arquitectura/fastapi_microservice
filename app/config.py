from pydantic import BaseSettings


class Settings(BaseSettings):
	app_name: str = "CIDS_FastAPI"
	DB_HOST: str = '0.0.0.0'
	DB_PORT: int = 1521
	DB_SID: str = 'ORCLDB'
	DB_USER: str = 'usr'
	DB_PASS: str = 'pass'
	DB_CONN_MIN: int = 1
	DB_CONN_MAX: int = 2
	REDIS_HOST: str = 'localhost'
	REDIS_PASSWORD: str = 'redistest'
	REDIS_PORT: int = 6379

	class Config:
		env_file = ".env"
