import os
import hikari
import lightbulb
import aiohttp
from dotenv import load_dotenv
from Liff import GUILD_ID

load_dotenv()

bot = lightbulb.BotApp(
    token=os.getenv("KEY"),
    prefix="-",
    banner=None,
    intents=hikari.Intents.ALL,
    default_enabled_guilds=GUILD_ID,
)

bot.load_extensions_from("Liff/extensions/", must_exist=True)


@bot.command
@lightbulb.command("ping", description="The bot's ping")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Pong! Latency: {bot.heartbeat_latency*1000:.2f}ms")


@bot.listen()
async def on_starting(event: hikari.StartingEvent) -> None:
    bot.d.aio_session = aiohttp.ClientSession()


@bot.listen()
async def on_stopping(event: hikari.StoppingEvent) -> None:
    await bot.d.aio_session.close()


if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()
    bot.run()
