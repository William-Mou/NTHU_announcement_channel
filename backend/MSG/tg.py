import telepot

def send_msg(office, title, link):
    bot = telepot.Bot(os.environ["TELEPOT_TOKEN"])

    try:
        bot.sendMessage(-1001429244108,  office + "公告：\n" + title +  "\n" + link)
        print("新增一筆新的文章：", title)
    except:
        print("time out :", title)
