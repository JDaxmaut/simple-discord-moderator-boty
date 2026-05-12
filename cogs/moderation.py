"""
Команды модерации: ban, kick.
"""

from discord.ext import commands


class Moderation(commands.Cog):
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member, *, reason="Нарушение правил"):
        await member.ban(reason=reason)
        await ctx.send(f"Пользователь {member} забанен")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member, *, reason="Нарушение правил"):
        await member.kick(reason=reason)
        await ctx.send(f"Пользователь {member} кикнут")


async def setup(bot):
    await bot.add_cog(Moderation())
