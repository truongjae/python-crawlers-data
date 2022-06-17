import facebook    #sudo pip install facebook-sdk
import pygame
from gtts import gTTS
import random
from random import randint
import os
from time import sleep as sl
import playsound
import threading
import kivy
kivy.require('2.0.0')
import kivymd
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from tkinter import messagebox
class ReadComment:
    def __init__(self,access_token,link):
        try:
            self.graph = facebook.GraphAPI(access_token)
            page_id, id_post = self.get_page_name(link)
            self.id_read = page_id+"_"+id_post
            self.check_break = False
        except:
            messagebox.showinfo("Lỗi","Token không đúng!")
    def get_page_name(self,link):
        link = link.split("/")
        profile = self.graph.get_object(link[len(link)-3])
        page_id = profile['id']
        id_post = link[len(link)-1]
        return page_id,id_post
    def comment_new(self):
        first_comments = self.graph.get_connections(id=self.id_read, connection_name="comments",limit=1000)['data']
        len_comment = len(first_comments)-1
        comment = first_comments[len_comment]['from']['name'] + "     "+first_comments[len_comment]['message']
        return comment
    def playmp3(self,comment):
        output = gTTS(comment,lang="vi", slow=False)
        output.save("filemp3.mp3")
        playsound.playsound("filemp3.mp3")
        os.remove("filemp3.mp3")
    def check_comment(self,arr,cmt):
        for i in arr:
            if i.lower() in cmt.lower():
                return True
        return False
    def read_comment(self,quantity,list_block):
        last_comment = ""
        while True:
            comment = self.comment_new()
            if last_comment != comment:
                if len(comment) < int(quantity):
                    self.playmp3(comment)
                    name = comment.split("     ")
                    name = name[0]
                    last_comment = comment
                    if self.check_comment(["google","gg"],comment):
                        self.playmp3("Chị chào em "+name)
                    elif self.check_comment(["hi","hello","chào","lô"],comment):
                        chao = ["Chào em "+name+"  -    - - - chia sẻ cho thầy đi","Chào em "+name+"  -    - - - xem live cùng thầy Tiến nhé"]
                        self.playmp3(random.choice(chao))
                    elif self.check_comment(["lồn","lol","loz","nồn","địt","dcm","đcm","cc","cặc","lon","óc","ngu","vcl","vc","cmm","cứt","chó"],comment):
                        self.playmp3("   ---- - - - chửi bậy là không tốt nhé "+name)
                    elif self.check_comment(["ido","yêu","ghê","hay"],comment):
                        self.playmp3(" -- - -- -   chào fan   "+name+"  - -- -  thầy Tiến chóp một thế giới")	
                    elif list_block != "":
                        list_block = list_block.split(",")
                        if self.check_comment(list_block,comment):
                            self.playmp3("-------- -- thằng lồn "+name+" sủa ít thôi")
                    else:
                        chao = ["Chào em "+name+"  -    - - - chia sẻ cho thầy đi","Chào em "+name+"  -    - - - xem live cùng thầy Tiến nhé"]
                        self.playmp3(random.choice(chao))
            if self.check_break:
                break
            sl(randint(12,14))
class ReadCommentGUI(MDApp):
    def read_thread(self):
        token = self.input_token.text
        link = self.input_link.text
        try:
        	quantity = int(self.input_quantity.text)
        except:
        	quantity = 100
        list_block = self.input_list_block.text
        if not self.check_break:
                self.check_break = True
                self.button_read_comment.text = "    DỪNG    "
                self.theme_cls.primary_palette = "Red"
                self.read_comment_class = ReadComment(token,link)
                self.read_comment_class.read_comment(quantity,list_block)
        else:
            self.check_break = False
            self.button_read_comment.text = "    ĐỌC BÌNH LUẬN    "
            self.theme_cls.primary_palette = "Blue"
            self.read_comment_class.check_break = True
    def read_comment(self,args):
        t = threading.Thread(target = self.read_thread)
        t.start()
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.check_break = False
        self.read_comment_class = None
        screen = MDScreen()
        size = (600, 750)
        top  = Window.top  * Window.size[1] / size[1]
        left = Window.left * Window.size[0] / size[0]
        Window.size = size
        Window.top  = top
        Window.left = left
        # logo
        screen.add_widget(Image(
            source="logo.png",
            pos_hint = {"center_x": 0.5, "center_y":0.75},
            ))
        #token
        self.input_token = MDTextField(
            on_text_validate = self.read_comment,
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.5},
            font_size = 20
        )
        self.input_token.hint_text ="Nhập Token Facebook"
        screen.add_widget(self.input_token)
        #link
        self.input_link = MDTextField(
            on_text_validate = self.read_comment,
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.4},
            font_size = 20
        )
        self.input_link.hint_text ="Nhập Link Livestream"
        screen.add_widget(self.input_link)
        # so luong 
        self.input_quantity = MDTextField(
            on_text_validate = self.read_comment,
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.3},
            font_size = 20
        )
        self.input_quantity.hint_text ="Giới hạn số lượng kí tự bình luận (Mặc định 100 kí tự)"
        screen.add_widget(self.input_quantity)

        ### danh sach den
        self.input_list_block = MDTextField(
            on_text_validate = self.read_comment,
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.2},
            font_size = 20
        )
        self.input_list_block.hint_text ="Danh sách đen (Nhập tên fb, cách nhau bởi dấu phẩy)"
        screen.add_widget(self.input_list_block)
        ## button 
        self.button_read_comment = MDFillRoundFlatButton(
            text="    ĐỌC BÌNH LUẬN    ",
            font_size = 25,
            pos_hint = {"center_x": 0.5, "center_y":0.1},
            on_press = self.read_comment
        )


        screen.add_widget(self.button_read_comment)
        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.1},
            theme_text_color = "Secondary"
        )

        self.converted = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)
        return screen
if __name__ == '__main__':
    try:
    	ReadCommentGUI().run()
    except:
    	pass