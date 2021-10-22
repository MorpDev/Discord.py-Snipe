@bot.event
async def on_message_delete(message):
  bot.deleted.append(message.content)
  bot.author.append(message.author.id)
  bot.time.append(datetime.datetime.timestamp(datetime.datetime.now()))
@bot.command()
async def snipe(ctx, i:int = None):
  if bot.deleted==[]:
    await ctx.send("Hiç Bir mesaj silinmedi!")
    return
  if i==None:
    f=len(bot.deleted)
    i=len(bot.deleted)-1
    a=bot.get_user(bot.author[i])
    e=bot.deleted[i]
    ts=round(bot.time[i])
    embed=discord.Embed(description=e)
    embed.set_author(name=f"Snipe 1/{f}", icon_url=a.avatar_url)
    embed.add_field(name='** **', value=f'Mesajı Silen **{a.name}#{a.discriminator}** on <t:{ts}:f>')
    embed.set_footer(text=f'Kullanan Kişi {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
  elif int(len(bot.deleted))>=i and i!=0:
    u=i
    f=len(bot.deleted)
    i=len(bot.deleted)-i
    a=bot.get_user(bot.author[i])
    e=bot.deleted[i]
    ts=round(bot.time[i])
    embed=discord.Embed(description=e)
    embed.set_author(name=f"Snipe {u}/{f}", icon_url=a.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    embed.add_field(name='** **', value=f'Mesajı Silen **{a.name}#{a.discriminator}** on <t:{ts}:f>')
    await ctx.send(embed=embed)
  elif i==0:
    await ctx.send("Geçerli bir sayı girin, 0 beklenen bir bağımsız değişken değil...")
  else:
    f=len(bot.deleted)
    await ctx.send(f"sadece benim tarafımdan izlenen `{f}` silinmiş mesajlar var")
    return
@snipe.error
async def snipe_error(ctx, error):
  if isinstance(error, commands.BadArgument):
    await ctx.send("En son silinen mesajı istiyorsanız sayı alanını boş bırakın veya gerçek bir sayı girin!")
 
