import os

APP_ENV = os.getenv("APP_ENV", "development")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "adlibitum")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_NAME = os.getenv("DATABASE_NAME", "ecommerce")
TEST_DATABASE_NAME = os.getenv("TEST_DATABASE_NAME", "ecommerce_test")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_DB = os.getenv("REDIS_DB", "0")
