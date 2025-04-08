from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Copyright import app

# Replace these with actual links
SUPPORT_CHANNEL = "https://t.me/SANATANI_TECH"
SUPPORT_GROUP = "https://t.me/SANATANI_SUPPORT"
OWNER_USERNAME = "SACHIN_SANATANI"

START_IMAGE = "https://files.catbox.moe/gs6je4.jpg"  # Your Image URL

@app.on_message(filters.command(["start", "help"]))
async def start_command(app, message):
    buttons = [
        [InlineKeyboardButton("📚 Help and command", callback_data="help_menu")],
        [InlineKeyboardButton("ALL APP'S", callback_data="show_apps")],
        [InlineKeyboardButton("Support", url=SUPPORT_GROUP),
         InlineKeyboardButton("Update", url=SUPPORT_CHANNEL)],
        [InlineKeyboardButton("👑 Owner", url=f"https://t.me/{OWNER_USERNAME}")]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await app.send_photo(
        chat_id=message.chat.id,
        photo=START_IMAGE,
        caption="👋 **Welcome!**\n\nUse the buttons below for help and support!",
        reply_markup=reply_markup
    )

@app.on_callback_query(filters.regex("help_menu"))
async def help_menu(app, callback_query):
    buttons = [
        [InlineKeyboardButton("📢 Support Channel", url=SUPPORT_CHANNEL)],
        [InlineKeyboardButton("💬 Support Group", url=SUPPORT_GROUP)],
        [InlineKeyboardButton("👑 Owner", url=f"https://t.me/{OWNER_USERNAME}")],
        [InlineKeyboardButton("🔙 Back", callback_data="start_menu")]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        "**📚 Help Menu**\n\nYahan apna help text likh le!",
        reply_markup=reply_markup
    )

@app.on_callback_query(filters.regex("start_menu"))
async def back_to_start(app, callback_query):
    buttons = [
        [InlineKeyboardButton("📚 Help and command", callback_data="help_menu")],
        [InlineKeyboardButton("ALL APP'S", callback_data="show_apps")],
        [InlineKeyboardButton("Support", url=SUPPORT_GROUP),
         InlineKeyboardButton("Update", url=SUPPORT_CHANNEL)],
        [InlineKeyboardButton("👑 Owner", url=f"https://t.me/{OWNER_USERNAME}")]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        "👋 **Welcome Back!**\n\nUse the buttons below for help and support!",
        reply_markup=reply_markup
    )
