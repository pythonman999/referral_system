from aiogram import Bot, Dispatcher
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    bot_username: SecretStr
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


config = Settings()

bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")
bot_username = config.bot_username.get_secret_value()
dp = Dispatcher()