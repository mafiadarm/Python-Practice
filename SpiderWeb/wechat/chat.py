

import os
import re
from wxpy import *
import datetime
# from analyze.PATH_SETTING import *
MULTIMEDIA = "wechat_photo/"  # 设置一个放图片，视频的文件夹
WORDS = "./words.txt"  # 存放信息的文本
if not os.path.exists(MULTIMEDIA):
    os.mkdir(MULTIMEDIA)


bot = Bot(cache_path=True)
# fo = ensure_one(bot.search(u"西谷实修群2•非学员"))
if not os.path.exists("files"):
    os.mkdir("files")


@bot.register()
def get_message(message):
    tt3 = str(message.type)
    tt4 = str(message.chat)
    tt5 = str(message.member)
    tt6 = str(message.text)

    r_nam = re.compile(r"[\u4e00-\u9fa5\w]+")
    r_mem = re.compile(r"[\u4e00-\u9fa5\w]+")
    # tt = re.compile(r"\w+")
    # dd = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    chat_name = "".join(r_nam.findall(tt4))[5:]
    member = "_".join(r_mem.findall(tt5))[7:]

    # chat_re = "_".join(tt.findall(tt4))
    # memb_re = "_".join(tt.findall(tt5))
    # text_re = "_".join(tt.findall(tt6))

    # date_now = dd.findall(str(datetime.datetime.now()))[0]

    if str(message.type) in ["Recording", "Video", "Picture", "Attachment"]:
        print(f"get {tt3} form {tt4} {tt5}", message.file_name)

        path = f"{MULTIMEDIA}{chat_name}_{member}_{message.file_name}"
        message.get_file(save_path=path)

        with open(f"{WORDS}", "a", encoding="utf-8") as rr:
            rr.write(f"message:{tt4}\t{tt5}\t{str(datetime.datetime.now())}\t{tt3}\n<|{path}|>\n{'-'*10}\n")

        # if chat_re and memb_re and text_re and tt3 and date_now:
        #     we.checkIn(chat_re, memb_re, text_re, tt3, date_now)

        print("Download ......")

    elif tt4 == "<Chat: None>":
        print("get a new!")
    else:
        with open(f"{WORDS}", "a", encoding="utf-8") as rr:
            rr.write(f"message:{tt4}\t{tt5}\t{str(datetime.datetime.now())}\t{tt3}\n<|{tt6}|>\n{'-'*10}\n")

        # if chat_re and memb_re and text_re and tt3 and date_now:
        #     we.checkIn(chat_re, memb_re, text_re, tt3, date_now)

        print(f"char={tt4}, member={tt5}, text={tt6}, type={tt3}")

    # we.conn.commit()


embed(shell="python")  # 启动
