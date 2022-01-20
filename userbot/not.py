# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

async def update_restart_msg(chat_id, msg_id):
    DEFAULTUSER = ALIVE_NAME or "Set `ALIVE_NAME` ConfigVar!"
    message = (
        f"**⚡𝕯𝖎𝖔𝖗-𝖀𝖇𝖔𝖙⚡ v{BOT_VER} Sedang berjalan!**\n\n"
        f"**Telethon:** {version.__version__}\n"
        f"**Python:** {python_version()}\n"
        f"**User:** {DEFAULTUSER}"
    )
    await bot.edit_message(chat_id, msg_id, message)
    return True


try:
    from userbot.modules.sql_helper.globals import delgvar, gvarstatus

    chat_id, msg_id = gvarstatus("restartstatus").split("\n")
    with bot:
        try:
            bot.loop.run_until_complete(update_restart_msg(int(chat_id), int(msg_id)))
        except BaseException:
            pass
    delgvar("restartstatus")
except AttributeError:
    pass


if not BOT_TOKEN is None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=BOT_TOKEN)
else:
    tgbot = None


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 5
    number_of_cols = 4
    global looters
    looters = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} {}".format(f"{EMOJI_HELP}", x, f"{EMOJI_HELP}"),
            data="ub_modul_{}".format(x),
        )
        for x in helpable_modules
    ]
    pairs = list(
        zip(
            modules[::number_of_cols],
            modules[1::number_of_cols],
            modules[2::number_of_cols],
        )
    )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⟨⟨", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    f"⍅ 𝗖𝗟𝗢𝗦𝗘 ⍆", data="{}_close({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "⟩⟩", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


with bot:
    try:

        dugmeler = CMD_HELP
        user = bot.get_me()
        uid = user.id
        logo = ALIVE_LOGO
        diorlogo = HELP_LOGO
        tgbotusername = BOT_USERNAME

        @tgbot.on(events.NewMessage(pattern="/start"))
        async def handler(event):
            await event.message.get_sender()
            text = (
                f"__Hey, I am using__  **⚡𝕯𝖎𝖔𝖗-𝖀𝖇𝖔𝖙⚡** \n\n"
                f"⚡ **Group Support :** [Fanda Support](t.me/fandasupport)\n"
                f"⚡ **Owner Repo :** [Fatur](t.me/uurfavboys1)\n"
                f"⚡ **Repo :** [DIOR-UBOT](https://github.com/DIORrios285/DIOR-BOT)\n"
            )
            await tgbot.send_file(
                event.chat_id,
                logo,
                caption=text,
                buttons=[
                        [
                             Button.url(f"sᴜᴘᴘᴏʀᴛ​",
                                        "t.me/fandasupport"),
                             Button.url(f"ᴜᴘᴅᴀᴛᴇs​",
                                        "t.me/fandaproject")],
                             [Button.url("ᴅᴇᴠᴇʟᴏᴘᴇʀ​",
                                        "t.me/uurfavboys1")],
                        ],
                      )

        @tgbot.on(events.InlineQuery)
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith("@Dior_ubot"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.photo(
                    file=diorlogo,
                    link_preview=False,
                    text=f"**inline DIOR-UBOT**\n\n**Owner** [FATUR](t.me/uurfavboys1)\n**Jumlah** `{len(dugmeler)}` Modules",
                    buttons=buttons,
                )
            elif query.startswith("repo"):
                result = builder.article(
                    title="Repository",
                    description="Repository ⚡𝕯𝖎𝖔𝖗-𝖀𝖇𝖔𝖙⚡",
                    url="https://t.me/fandaproject",
                    text="**⚡𝕯𝖎𝖔𝖗-𝖀𝖇𝖔𝖙⚡**\n➖➖➖➖➖➖➖➖➖➖\n**Owner :** [FATUR](https://t.me/uurfavboys1)\n**Repository :** [⚡DIOR-UBOT⚡](https://github.com/DIORrios285/DIOR-UBOT)\n➖➖➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url("ɢʀᴏᴘ", "https://t.me/fandasupport"),
                            custom.Button.url(
                                "ʀᴇᴘᴏ", "https://github.com/DIORrios285/DIOR-UBOT"
                            ),
                        ],
                    ],
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="⚡𝕯𝖎𝖔𝖗-𝖀𝖇𝖔𝖙⚡",
                    description="DIOR-UBOT | Telethon",
                    url="https://t.me/fandasupport",
                    text=f"**DIOR-UBOT**\n➖➖➖➖➖➖➖➖➖➖\n**OWNER:** [FATUR](t.me/uurfavboys1)\n**Bot of:** {tgbotusername}\n➖➖➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url("ɢʀᴜᴘ", "https://t.me/fandasupport"),
                            custom.Button.url("ʀᴇᴘᴏ", "https://github.com/DIORrios285/DIOR-UBOT"),
                        ],
                    ],
                    link_preview=False,
                )
            await event.answer(
                [result], switch_pm="👥 USERBOT PORTAL", switch_pm_param="start"
            )

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"nepo")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            current_page_number = int(looters)
            buttons = paginate_help(current_page_number, dugmeler, "helpme")
            await event.edit(
                file=diorlogo,
                buttons=buttons,
                link_preview=False,
            )

        @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith("@Ram_ubot"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.photo(
                    file=diorlogo,
                    link_preview=False,
                    text=f"Usᴇʀʙᴏᴛ Tᴇʟᴇɢʀᴀᴍ\n\n❥ **ʙᴏᴛ ᴏꜰ :** {DEFAULTUSER}\n❥ **ʙᴏᴛ ᴠᴇʀ :** 8.0.0\n❥ **ᴍᴏᴅᴜʟᴇꜱ :** {len(plugins)}\n❥ @fandasupport".format(
                        len(dugmeler),
                    ),
                    buttons=buttons,
                )
            elif query.startswith("tb_btn"):
                result = builder.article(
                    "Bantuan Dari {REPO_NAME}",
                    text="Daftar Plugins",
                    buttons=[],
                    link_preview=True)
            else:
                result = builder.article("{REPO_NAME}",
                                         text="""𝕯𝖎𝖔𝖗-𝖀𝖇𝖔𝖙""",
                                         buttons=[[custom.Button.url("ꜰᴀᴛᴜʀ​",
                                                                     "t.me/uurfavboys1"),
                                                   custom.Button.url("ɢʀᴜᴘ​",
                                                                     "t.me/fandasupport"),
                                                   ],
                                                  [custom.Button.url("ʟɪᴄᴇɴsᴇ​",
                                                                     "https://github.com/DIORrios285/DIOR-UBOT/LICENSE",
                                                                     )],
                                                  ],
                                          link_preview=False,
                                          )
            await event.answer([result] if result else None)


        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_close\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # @Ram_ubot
                # https://t.me/TelethonChat/115200
                await event.edit(
                    file=diorlogo,
                    link_preview=True,
                    buttons=[
                        [
                            Button.url("Sumbang Kosa kata",
                                       "t.me/requestkatakatalubot"),],
                        [
                            Button.url("Support",
                                       "t.me/fandasupport"),
                            Button.url("Updates",
                                       "t.me/fandaproject")],
                        [custom.Button.inline(
                            "Open Menu", data="open_plugin")],
                        [custom.Button.inline(
                            "Close", b"close")],
                    ]
                )

        @tgbot.on(events.CallbackQuery(data=b"close"))
        async def close(event):
            buttons =[
                [custom.Button.inline("Open Menu", data="nepo")],
            ]
            await event.edit("Menu Ditutup!", buttons=buttons.clear())

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme"  # pylint:disable=E0602
                )
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"ub_modul_(.*)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 180:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace(
                            '`', '')[:180] + "..."
                        + "\n\nBaca Text Berikutnya Ketik .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = str(CMD_HELP[modul_name]).replace('`', '')

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} No document has been written for module.".format(
                        modul_name
                    )
                )
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."

            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    except BaseException:
        LOGS.info(
            "Mode Inline Bot Mu Nonaktif. "
            "Untuk Mengaktifkannya, Silahkan Pergi Ke @BotFather Lalu, Settings Bot > Pilih Mode Inline > Turn On. ")
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID Environment Variable Isn't a "
            "Valid Entity. Please Check Your Environment variables/config.env File.")
        quit(1)
