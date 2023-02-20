import os

chat_language = os.getenv("INIT_LANGUAGE", default = "zh")

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 20))
LANGUAGE_TABLE = {
  "zh": "嗨！",
  "en": "Hi!"
}

Prompt = ( 使用專業的人資口吻回答
          "Q:想問何時能得到這個職位是否錄取的答覆"
          "A:您好，公司將進行履歷審核以及彙整主管意見，將於10天內回覆您面試的結果"
          "Q:想問加班費怎麼算"
          "A:您好，公司的加班費率依照勞基法計算，將依當天是休息日或是國定假日而定"
          )
  
    def __init__(self):
        self.msg_list = []
        self.msg_list.append(f"AI:{LANGUAGE_TABLE[chat_language]}")
    
    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.remove_msg()
        self.msg_list.append(new_msg)

    def remove_msg(self):
        self.msg_list.pop(0)

    def generate_prompt(self):
        return '\n'.join(self.msg_list)
