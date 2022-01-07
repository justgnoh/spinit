import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import seed
from random import randint

bot = telebot.TeleBot("TOKEN", parse_mode=None) 
# You can set parse_mode by default. HTML or MARKDOWN

seed(1)

class Food:
    def __init__(self, name, address, hours, website, keywords):
        self.name = name
        self.address = address
        self.hours = hours
        self.website = website
        self.keywords = keywords

class Lifestyle:
    def __init__(self, name, address, hours, website, price):
        self.name = name
        self.address = address
        self.hours = hours
        self.website = website
        self.price = price

class OutAndAbout:
    def __init__(self, name, address, hours, website, price, keywords):
        self.name = name
        self.address = address
        self.hours = hours
        self.website = website
        self.price = price
        self.keywords = keywords

#################
# Database
#################

# name, address, opening hours, website, keywords
food_lunch_list = [
    Food("Carrot Cubes", "Blk 527 Ang Mo Kio Avenue 10 #01-115 Cheng San Market", "0900-1400", "None", ["Hawker", "Modern"]),
    Food("Ah Hua Teochew Fishball Noodle", "415 Pandan Gardens, #01-117, Singapore 600415", "0800 - 1500", "None", ["Chinese", "Hawker", "Affordable"]),
    Food("Nice Rice", "802 French Rd, 01-69 Block 802, Singapore 200802", "1100 - 1500", "None", ["ricebowl", "japanese", "french", "hawker", "affordable"]),
    Food("Park Bench Deli", "179 Telok Ayer Street ", "0900-1730", "None", ["western", "sandwich", "grabngo"])
]

food_cafesnack_list = [
    Food("Poh Cheu Kitchen", "Block 127, Bukit Merah Lane 1, #01-222, Singapore 150127", "1100 - 1630", "None", ["traditional", "hawker"]),
    Food("Brotherbird Bakehouse", "CT Hub 2, 114 Lavender Street #01-05", "1100 - 1630", "None", ["croissant", "pastry"]),
    Food("Le Matin Patisserie", "None", "None", "www.lematinpatisserie.com", ["fancy", "unique", "pastry"]),
    Food("Starter Lab Bakery", "721 Havelock Rd, Singapore 169645", "0830 - 1700", "None", ["sourdough", "bread", "coffee"]),
    Food("The Fat Kid Bakery", "7 Ang Mo Kio Street 66, #01-07, Singapore 567708", "1000 - 1700", "None", ["simple", "bread", "brownies"])
]

food_dinner_list = [
    Food("Shashlik Restaurant", "545 Orchard Road, #06-19 Far East Shopping Centre, 238882", "1200 - 1400, 1800 - 2100", "None", ["fusion", "russian", "hainanese", "oldschool"]),
    Food("Lad & Dad", "1 Kadayanallur Street, Maxwell Food Centre, Stall 79, Singapore 069184", "1830 - 2130", "None", ["western", "hawker"]),
    Food("Kin", "Straits Clan Lobby, 31 Bukit Pasoh Road", "None", "None", ["cantonese", "fusion", "fancy"]),
    Food("Po", "The Warehouse Hotel, 320 Havelock Road, Robertson Quay", "0900-1730", "None", ["chinese", "fancy", "fusion"]),
    Food("Two Bakers", "9 Teck Chye Terrace, Singapore 545720", "1000 - 2130", "None", ["fusion", "western", "japanese"])
]

lifestyle_list = [
    Lifestyle("Terrarium-making workshop", "The Green Capsule, 107 North Bridge Rd, #04-11 Funan, Singapore 179105", "1130 - 2000", "www.thegreencapsule.com.sg", "$"),
    Lifestyle("Art Jamming", "Cafe de Paris, 313 Orchard Road, 313@Somerset, #B1-37, Singapore 238895", "1100 - 2200", "https://www.facebook.com/cafedeparissg/", "$22 to $30"),
    Lifestyle("Baking class", "The Vanilla Beans SG, 767 Upper Serangoon Road #02-11, Spazio@Kovan", "None", "www.vanillabeansg.com", "$100 to $250")
]

out_and_about_list = [
    OutAndAbout("SkyHelix Sentosa", "41 Imbiah Rd, Sentosa, 099707", "1000 - 2100", "None", "$18", ["adventure", "outdoors"]),
    OutAndAbout("Pop-up Disney Exhibition", "Suntec Convention Centre, Level 3, 1 Raffles Boulevard, Suntec City, Singapore 039593", "1100 - 2100", "None", "$26", ["childhood", "animation"]),
    OutAndAbout("National Gallery", "1 St Andrew's Rd, #01 – 01, Singapore 178957", "1000 - 1900", "None", "free for Singaporeans", ["art", "history"]),
    OutAndAbout("Street art hunting", "Various places, Haji Lane, Chinatown", "All-Day", "None", "free", []),
    OutAndAbout("The Cat Cafe Singapore", "241B Victoria Street Level 3", "1000 - 2200", "None", "$16 to $25 ", ["animals", "indoors"])
]

print("Telegram Bot is running...")

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Food 🍰", callback_data="cb_food"),
                               InlineKeyboardButton("Lifestyle 🚲⛷🎨", callback_data="cb_lifestyle"),
                               InlineKeyboardButton("Out & About 🎭", callback_data="cb_activity"))
    return markup

def foodtime_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Lunch", callback_data="get_lunch"),
                               InlineKeyboardButton("Cafe/Snack", callback_data="get_cafesnack"),
                               InlineKeyboardButton("Dinner", callback_data="get_dinner"))
    return markup

def createMessage(object, type):
    if(type == "Lifestyle"):
        message = "Here is your " + type + " recco!" + "\n\n" + "<b>" + object.name + "</b>" + "\n \n" + "Address: " + object.address + "\n" + "Operating Hours: " + object.hours + "\n" + "Website: " + object.website + "\n" + "Price: " + object.price
        return message

    elif (type == "Lunch" or type == "Cafe/Snack" or type == "Dinner"):
        if(len(object.keywords) > 0):
            keywords = ""
            for x in object.keywords:
                keywords += "#" + x + " "

        message = "Here is your " + type + " recco!" + "\n\n" + "<b>" + object.name + "</b>" + "\n \n" + "Address: " + object.address + "\n" + "Operating Hours: " + object.hours + "\n" + "Website: " + object.website + "\n" + "Keywords: " + keywords

        return message

    elif (type == "Activity"):
        if(len(object.keywords) > 0):
            keywords = ""
            for x in object.keywords:
                keywords += "#" + x + " "

        message = "Here is your " + type + " recco!" + "\n\n" + "<b>" + object.name + "</b>" + "\n \n" + "Address: " + object.address + "\n" + "Operating Hours: " + object.hours + "\n" + "Website: " + object.website + "\n" + "Keywords: " + keywords

        return message


### Global Variable
message_chat_id = 0

@bot.message_handler(commands=['spin'])
def start_handler(message):
    global message_chat_id 
    message_chat_id = message.chat.id
    bot.send_message(message.chat.id, "Please select a category you would like a recco for! 😀" , reply_markup=gen_markup())

@bot.message_handler(commands=['help'])
def help_handler(message):
    help_message = "❓ Try typing /spin to begin! ❓"
    bot.send_message(message.chat.id, help_message)

@bot.message_handler(commands=['suggest'])
def suggest_handler(message):
    suggest_message = "<b>" + "[This feature is a WORK-IN-PROGRESS]" + "</b>" + "\n\n" + "Users will be able to fill up a form facilitated by the bot to suggest a spot to the existing repository." + "\n\n" + "Thank you for your contribution! The team will review your submission and be in contact with you soon!"
    bot.send_message(message.chat.id, suggest_message, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global message_chat_id 

    if call.data == "cb_food":
        # Trigger food timing selection
        bot.send_message(message_chat_id, "Please select an option! 😀", reply_markup=foodtime_markup())
        bot.answer_callback_query(call.id, "Selected food option...")

    elif call.data == "cb_lifestyle":
        value = randint(0,len(lifestyle_list)-1)
        message = createMessage(lifestyle_list[value], "Lifestyle")
        bot.send_message(message_chat_id, message, parse_mode="HTML")
        bot.answer_callback_query(call.id, "Sending you a Lifestyle recco...")

    elif call.data == "cb_activity":
        value = randint(0,len(out_and_about_list)-1)
        message = createMessage(out_and_about_list[value], "Activity")
        bot.send_message(message_chat_id, message, parse_mode="HTML")
        bot.answer_callback_query(call.id, "Sending you an Activity recco...")

    elif call.data == "get_lunch":
        value = randint(0,len(food_lunch_list)-1)
        message = createMessage(food_lunch_list[value], "Lunch")
        bot.send_message(message_chat_id, message, parse_mode="HTML")
        bot.answer_callback_query(call.id, "Sending you a Lunch recco...")

    elif call.data == "get_cafesnack":
        value = randint(0,len(food_cafesnack_list)-1)
        message = createMessage(food_cafesnack_list[value], "Cafe/Snack")
        bot.send_message(message_chat_id, message, parse_mode="HTML")
        bot.answer_callback_query(call.id, "Sending you a Cafe/Snack recco...")

    elif call.data == "get_dinner":
        value = randint(0,len(food_dinner_list)-1)
        message = createMessage(food_dinner_list[value], "Dinner")
        bot.send_message(message_chat_id, message, parse_mode="HTML")

        bot.answer_callback_query(call.id, "Sending you Dinner recco...")
   

bot.infinity_polling()



