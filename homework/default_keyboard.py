from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("Computer Engineering"), KeyboardButton("Graphic design")],
    [KeyboardButton("Programming"), KeyboardButton("Trading")],
    [KeyboardButton("Logistics")]]
    , resize_keyboard=True)

inside_ce = ReplyKeyboardMarkup([[KeyboardButton("Back")]], resize_keyboard=True)
inside_gd = ReplyKeyboardMarkup([[KeyboardButton("Back")]], resize_keyboard=True)
inside_prg = ReplyKeyboardMarkup([[KeyboardButton("Back")]], resize_keyboard=True)
inside_l = ReplyKeyboardMarkup([[KeyboardButton("Back")]], resize_keyboard=True)
inside_tr = ReplyKeyboardMarkup([[KeyboardButton("Back")]], resize_keyboard=True)

computer_engineering = InlineKeyboardMarkup(row_width=2)
computer_engineering.add(InlineKeyboardButton(text="Learning PC from 0", url="https://www.youtube.com/results?search_query=Learning+PC+from+0"),
                         InlineKeyboardButton(text="How to set windows", url="https://www.youtube.com/results?search_query=How+to+set+windows"))

graphic_design = InlineKeyboardMarkup(row_width=2)
graphic_design.add(InlineKeyboardButton(text="Adobe Photoshop", url="https://www.youtube.com/results?search_query=Adobe+Photoshop"),
                   InlineKeyboardButton(text="Figma", url="https://www.youtube.com/results?search_query=figma"))

programming = InlineKeyboardMarkup(row_width=2)
programming.add(InlineKeyboardButton(text="Python", url="https://www.youtube.com/watch?v=NpmFbWO6HPU"),
                InlineKeyboardButton(text="C++", url="https://www.youtube.com/watch?v=8jLOx1hD3_o&t=2458s"),
                InlineKeyboardButton(text="Java", url="https://www.youtube.com/watch?v=bm0OyhwFDuY&list=PLsyeobzWxl7pe_IiTfNyr55kwJPWbgxB5"),
                InlineKeyboardButton(text="C#", url="https://www.youtube.com/watch?v=9THmGiSPjBQ&list=PLdo4fOcmZ0oULFjxrOagaERVAMbmG20Xe"))

trading = InlineKeyboardMarkup(resize_keyboard=True)
trading.add(InlineKeyboardButton(text="Trading for beginners", url="https://www.youtube.com/watch?v=_YVQN6_nkfs"),
            InlineKeyboardButton(text="Trading for intermediates", url="https://www.youtube.com/watch?v=gcMKdkCdwdY&list=PLv-X125JpAa2wX8f05GryHEK5b4O2LyTF"))

logistics = InlineKeyboardMarkup(resize_keyboard=True)
logistics.add(InlineKeyboardButton(text="Logistics for beginners", url="https://www.youtube.com/watch?v=4-QU7WiVxh8&list=PL6HtN7XnHCF6aAiOfQ9l4WaOMrA3n3H6E"),
              InlineKeyboardButton(text="Logistics for intermediates", url="https://www.youtube.com/results?search_query=logistics+for+intermediate"))



