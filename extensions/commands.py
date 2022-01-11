import hikari
import lightbulb

commands_plugin = lightbulb.Plugin("Commands")

@commands_plugin.command
@lightbulb.command("commands", "IDK what to put here")
@lightbulb.implements(lightbulb.SlashCommandGroup, lightbulb.PrefixCommandGroup)
async def commands_group(ctx: lightbulb.Context) -> None:
    pass  # as slash commands cannot have their top-level command ran, we simply pass here


@commands_group.child
@lightbulb.command("meme", "Fetch a meme")
@lightbulb.implements(lightbulb.SlashSubCommand, lightbulb.PrefixSubCommand)
async def meme_subcommand(ctx: lightbulb.Context) -> None:
    async with ctx.bot.d.aio_session.get(
        "https://meme-api.herokuapp.com/gimme"
    ) as response:
        res = await response.json()
        if response.ok and res["nsfw"] != True:
            link = res["postLink"]
            title = res["title"]
            img_url = res["url"]
            embed = hikari.Embed(colour=0x3B9DFF)
            embed.set_author(name=title, url=link)
            embed.set_image(img_url)
            await ctx.respond(embed)
        else:
            await ctx.respond(
                "Could not fetch a meme :c", flags=hikari.MessageFlag.EPHEMERAL
            )

@commands_plugin.command
@lightbulb.command("idk", "Yep Front")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def idk_wtf(ctx: lightbulb.Context) -> None:
    await ctx.respond("yep front")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(commands_plugin)
