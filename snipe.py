async def discord_user(user_id):
    header= {"Yetki":"Bot [token, ayrıca Bot bir bot hesabıysa başlangıçta orada olurdu]"}
    a = aiohttp.ClientSession(headers=header)
    response = await a.get(f"https://discord.com/api/v9/users/{user_id}",headers=header)
    response =  await response.json()
    if str(response["avatar"]).startswith("a_"):
        avatar = "https://cdn.discordapp.com/avatars/{0}/{1}.gif?size=1024".format(user_id,response["avatar"])
    else:
        avatar = "https://cdn.discordapp.com/avatars/{0}/{1}.png?size=1024".format(user_id,response["avatar"])

    if response["banner"] == None:
        banner = None
    elif str(response["banner"]).startswith("a_"):
        banner = "https://cdn.discordapp.com/banners/{0}/{1}.gif?size=1024".format(user_id,response["banner"])
    else:
        banner = "https://cdn.discordapp.com/banners/{0}/{1}.png?size=1024".format(user_id,response["banner"])
    await a.close()
    a = response
    a["avatar"] = avatar
    a["banner"] = banner
    return a
 
