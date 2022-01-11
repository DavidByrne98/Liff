import hikari
import lightbulb

info_plugin = lightbulb.Plugin("Music")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(info_plugin)

