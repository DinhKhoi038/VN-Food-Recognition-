import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tensorflow as tf
import qrcode
import numpy as np
import re
from tensorflow import keras
from tensorflow.keras.utils import load_img, img_to_array
import webbrowser
from googletrans import Translator


#Load Model----------------------------------------------------------------------------------------------------
new_model = tf.keras.models.load_model("d:\Downloads\FoodRec\FoodRec.h5")

#Def cac button-------------------------------------------------------------------
#Def Button openimage
def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()
    

    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                       filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 800 # Processing image for displaying
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel_image = tk.Label(frame, image=img).pack()
    frame.config(bg= 'black')

#Def Button Classify
def classify():
    global tendoan, y_predsforprinted, label2, label3, image_batch
    original = Image.open(image_data)
    original = original.resize((150, 150), Image.ANTIALIAS)
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    #processed_image = new_model.preprocess_input(image_batch.copy())
    result = new_model.predict(image_batch)
    global prediction, sub_prediction
    if round(result[0][0]) == 1:
        prediction = 'Bánh bèo'
    if round(result[0][1]) == 1:
        prediction = 'Bánh bột lọc'
    if round(result[0][2]) == 1:
        prediction = 'Bánh căn'
    if round(result[0][3]) == 1:
        prediction = 'Banh canh'
    if round(result[0][4]) == 1:
        prediction = 'Bánh chưng' 
    if round(result[0][5]) == 1:
        prediction = 'Bánh cuốn'
    if round(result[0][6]) == 1:
        prediction = 'Bánh đúc'
    if round(result[0][7]) == 1:
        prediction = 'Bánh giò'
    if round(result[0][8]) == 1:
        prediction = 'Bánh khọt'
    if round(result[0][9]) == 1:
        prediction = 'Bánh mì'
    if round(result[0][10]) == 1:
        prediction = 'Bánh pía'
    if round(result[0][11]) == 1:
        prediction = 'Bánh tét'
    if round(result[0][12]) == 1:
        prediction = 'Bánh tráng nướng'
    if round(result[0][13]) == 1:
        prediction = 'Bánh xèo'
    if round(result[0][14]) == 1:
        prediction = 'Bún bò huế'
    if round(result[0][15]) == 1:
        prediction = 'Bún đậu mắm tôm' 
    if round(result[0][16]) == 1:
        prediction = 'Bún mắm'
    if round(result[0][17]) == 1:
        prediction = 'Bún riêu'
    if round(result[0][18]) == 1:
        prediction = 'Bún thịt nướng'
    if round(result[0][19]) == 1:
        prediction = 'Cá kho tộ'
    if round(result[0][20]) == 1:
        prediction = 'Canh chua'
    if round(result[0][21]) == 1:
        prediction = 'Cao lầu'
    if round(result[0][22]) == 1:
        prediction = 'Cháo lòng'
    if round(result[0][23]) == 1:
        prediction = 'Cơm tấm'
    if round(result[0][24]) == 1:
        prediction = 'Gỏi cuốn'
    if round(result[0][25]) == 1:
        prediction = 'Hủ tiếu'
    if round(result[0][26]) == 1:
        prediction = 'Mì Quảng' 
    if round(result[0][27]) == 1:
        prediction = 'Nem chua'
    if round(result[0][28]) == 1:
        prediction = 'Phở'
    if round(result[0][29]) == 1:
        prediction = 'Xôi xéo'
    print("Đây là :", str(prediction).upper())

    #Hien thi len window 1
    cau1 = Label(wd, text = 'Hmm..., it looks a lot like:',bg = 'white', fg = 'midnightblue', font = ("Arial", 12 ))
    cau1.place(x= 20, y = 550)

    tendoan = tk.Label(wd, text = str(prediction).upper(), bg = 'white',fg = 'midnightblue', font= ("Helvetica 18 bold", 22), borderwidth=2, relief="ridge")
    tendoan.place(x= 20, y = 580, width = 345, height = 50)

        #trich xuat url
    url = 'https://www.google.com/search?&q=Cách+nấu+'+re.sub("\s+","+",prediction) #ham RegEx đe thay the ki tu
    print(url)
    #Tao qrcode tu url
    qr_inputurl = url
    qr = qrcode.QRCode(version=1, box_size=2, border=1)
    qr.add_data(qr_inputurl)
    qr.make(fit = True)
    qr_image = qr.make_image(fill='black', back_color = 'white')
    qr_image.save("C:\\Users\\Admin\\qrcode002.png")

    photo = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\qrcode002.png"))
    label2 = tk.Label(wd, image=photo)
    label2.image = photo
    label2.place(x = 280, y = 455 )

    label3 = Label(wd, text= "SCAN THIS", fg = 'black', bg='white', font=('Arial', 8))
    label3.place(x = 290, y = 434)

    #messagebox
    messagebox.showinfo("PROCESSING","Detecting is done")


ham = {"Bún bò huế":"Bún bò là một trong những đặc sản của xứ Huế, mặc dù món bún này phổ biến trên cả ba miền ở Việt Nam và cả người Việt tại hải ngoại. Tại Huế, món này được gọi đơn giản là 'bún bò' hoặc gọi cụ thể hơn là 'bún bò thịt bò'. Các địa phương khác gọi là 'bún bò Huế', 'bún bò gốc Huế' để chỉ xuất xứ của món ăn này.. Hương vị: vị cay nồng, mùi sả đặc trưng của nước lèo.",
'Bánh bèo':"Bánh bèo là một món bánh xuất thân từ Cố Đô Huế rất thịnh hành ở miền Trung, ngoài ra cũng phổ biến ở miền Nam Việt Nam. Bánh bèo đã trở thành một nét đẹp trong văn hóa ẩm thực của người dân Viêt Nam từ bao đời nay. Tên bánh bèo có thể xuất phát từ hình dạng của nó: giống như cái lá của cây bèo.",
"Bánh bột lọc":"Bánh bột lọc thường được hấp hoặc luộc, và gói bằng lá chuối. Nếu gói bằng lá chuối, thì gọi là bánh bột lọc lá. Nếu không có lá chuối gói lại thì gọi là bánh bột lọc trần. Nhân bánh theo truyền thống là một con tôm nướng nguyên vỏ và một lát thịt lợn",
"Bánh căn":"Bánh căn là một loại bánh phổ biến của Ninh Thuận. Vì bánh căn nhỏ nên thường tính theo cặp chứ không theo cái, ở giữa có thể quét mỡ hành hoặc đổ trứng. Bánh căn thường ít được dọn cùng rau sống ăn lá, mà thường ăn kèm với xoài xanh, khế chua, dưa leo băm sợi.",
"Banh canh":"Bánh canh là một món ăn Việt Nam. Bánh canh có nguồn gốc từ Đông Nam Bộ, sau đó phổ biến khắp Việt Nam. Bánh canh bao gồm nước dùng được nấu từ tôm, cá và giò heo thêm gia vị tùy theo từng loại bánh canh. Sợi bánh canh có thể được làm từ bột gạo, bột mì, bột năng hoặc bột sắn hoặc bột gạo pha bột sắn.",
'Bánh chưng':"Bánh chưng là một loại bánh truyền thống của dân tộc Việt nhằm thể hiện lòng biết ơn của con cháu đối với cha ông với đất trời. Nguyên liệu làm bánh chưng gồm gạo nếp, đậu xanh, thịt lợn, lá dong. Bánh thường được làm vào các dịp Tết của dân tộc Việt, cũng như ngày giỗ tổ Hùng Vương.",
"Bánh cuốn":"Bánh cuốn, còn gọi là bánh mướt hay bánh ướt, là một món ăn làm từ bột gạo hấp tráng mỏng, cuộn tròn, bên trong độn nhân rau hoặc thịt.",
"Bánh đúc":"Bánh đúc là một loại bánh của Việt Nam, thường được làm bằng bột gạo hoặc bột năng với một số gia vị. Bánh được làm thành tấm to, khi ăn thì cắt nhỏ thành miếng tùy thích. Là món ăn dân dã thịnh hành khắp ba miền, bánh đúc ăn giòn, mát, mịn, no bụng mà lại dễ tiêu, dễ làm và giá thành cũng rất rẻ.",
"Bánh giò":"Bánh giò là một loại bánh được làm bằng bột gạo tẻ, bột năng hòa với nước xương hầm, nhân làm từ thịt nạc vai có kèm mộc nhĩ, hành tím khô, hành ta, hạt tiêu, nước mắm, muối, Bánh giò có hình dài nhô cao như hình bàn tay úp khum khum với các ngón tay sát nhau, bánh được gói bằng lá chuối và hấp bằng chõ",
"Bánh khọt":"Bánh khọt là loại bánh Việt Nam làm từ bột gạo hoặc bột sắn, có nhân tôm, được nướng và ăn kèm với rau sống, ớt tươi, thường ăn với nước mắm pha ngọt, rất ít khi chấm nước sốt mắm tôm.",
"Bánh mì":"Bánh mì Việt Nam (gọi tắt là bánh mì) là một món ăn Việt Nam, với lớp vỏ ngoài là một ổ bánh mì nướng có da giòn, ruột mềm, còn bên trong là phần nhân. Tùy theo văn hóa vùng miền hoặc sở thích cá nhân, người ta có thể chọn nhiều nhân bánh mì khác nhau. Tuy nhiên, loại nhân bánh truyền thống thường chứa chả lụa, thịt, cá, thực phẩm chay hoặc mứt trái cây, kèm theo một số nguyên liệu phụ khác như patê, bơ, rau, ớt và đồ chua.",
"Bánh pía":"Bánh pía tiếng Trung: 朥饼; Bạch thoại tự: hó-piáⁿ là món bánh ngọt ngàn lớp có nhân và là bánh trung thu truyền thống xuất phát từ Triều Châu, Trung Quốc và được du nhập vào các khu phố người Hoa trên thế giới. Đặc biệt ở Đông Nam Á, nơi có Hoa Kiều cư ngụ là Malaysia, Indonesia, Philippines và Singapore",
"Bánh tét":"Bánh tét, có nơi gọi là bánh đòn, là một loại bánh trong ẩm thực của cả người Việt và một số dân tộc ít người ở miền Nam và miền Trung Việt Nam, là nét tương đồng của bánh chưng ở Miền Bắc về nguyên liệu, cách nấu, chỉ khác về hình dáng và sử dụng lá chuối để gói thay vì lá dong",
"Bánh tráng nướng":"Nó được làm từ loại bánh tráng mỏng nướng giòn với phần nhân bánh phong phú như xúc xích, gà xé, thập cẩm, hải sản, khô bò, phô mai, trứng gà..., tương tự như kiểu bánh pizza của Ý và rưới kèm nước sốt (tương ớt và sốt me).",
"Bánh xèo":"Ở miền Trung, bánh xèo thường có kích thước nhỏ gọn. Nhân thường được làm từ thịt heo hoặc tôm. Ngoài ra ngày nay bánh xèo còn được chế biến với nhân nấm, thịt vịt… Đặc điểm đặc trưng của bánh xèo miền Trung đó là phần vỏ bánh không quá dày cũng không quá mỏng. Bánh đổ ra thường mềm, hơi dẻo khi ăn. Người dân địa phương thường để bánh xèo vào chén hoặc đĩa rồi ăn chung với rau sống và nước chấm.",
"Bún đậu mắm tôm":"Bún đậu mắm tôm là món ăn đơn giản, dân dã trong ẩm thực miền Bắc Việt Nam. Đây là món thường được dùng như bữa ăn nhẹ, ăn chơi. Thành phần chính gồm có bún tươi, đậu hũ chiên vàng, chả cốm, nem chua,dồi chó, mắm tôm pha chanh, ớt và ăn kèm với các loại rau thơm như tía tô, kinh giới, rau húng, xà lách, cà pháo...",
"Bún mắm":"Bún mắm là món đặc sản ở miền Tây Nam Bộ, món ăn này có xuất xứ từ Campuchia. Với phiên bản gốc thường được nấu bằng mắm bù hốc và khi sang Việt Nam thì được nấu bằng mắm cá linh hoặc mắm cá sặc. Bún mắm nấu không khó nhưng phải biết cách canh tỷ lệ mắm - nước sau cho món ăn không bị quá mặn. Cùng xem tiếp để biết cách nấu món ăn đặc sản này nhé!",
"Bún riêu":"Bún riêu cua là một món ăn truyền thống Việt Nam, được biết đến rộng rãi trong nước và quốc tế. Món ăn này gồm bún (bún rối hoặc bún lá) và 'riêu cua'. Riêu cua là canh chua được nấu từ gạch cua, thịt cua giã và lọc cùng với quả dọc, cà chua, mỡ nước, giấm bỗng, nước mắm, muối, hành hoa.",
"Bún thịt nướng":"Bún thịt nướng là một món ăn có nguồn gốc ở miền Nam Việt Nam, về sau đã phổ biến lan rộng tại nhiều nơi trên cả nước. Mỗi nơi đều có thể có cho mình một hương vị đặc trưng riêng tùy theo khẩu vị từng nơi. Món bún này có thể dùng làm điểm tâm, bữa chính hay bữa phụ đều phù hợp.",
"Cá kho tộ":"Cá kho tộ vốn là món ăn dân dã của người dân vùng sông nước miền tây nam bộ. Thường xuất hiện trong bữa cơm hàng ngày của nhiều gia đình, những niêu cá kho chinh phục người ăn bằng hương vị đậm đà, béo ngậy, thơm ngon và đặc biệt “tốn cơm”.",
"Canh chua":"Canh chua là tên gọi của những món ăn nhiều nước và có vị chua do được nấu bằng các nguyên liệu phối trộn với gia vị tạo chua. Canh chua thường được dùng ở những vùng nóng như miền Nam, miền Trung, hoặc những lúc nóng nực của mùa hè miền Bắc Việt Nam. Theo định nghĩa của Từ điển tiếng Việt thì riêu là món ăn lỏng nấu bằng cua hoặc cá với chất chua và gia vị. Do đó nguyên liệu chính để nấu canh chua là loại rau củ quả, các loại thịt hay thủy sản (cá, tôm, cua, ốc, hến, trai, sò) khác nhau, trong đó thường dùng một gia vị chua để tạo vị chua thơm ngon cho nước canh.",
"Cao lầu":"Cao lầu là một món mì ở Quảng Nam, Việt Nam. Đây được xem là món ăn đặc sản của thành phố Hội An. Món mì này có sợi mì màu vàng, được dùng với tôm, thịt heo, các loại rau sống và rất ít nước dùng. Sợi mì màu vàng là do được trộn với tro từ một loại cây ở địa phương.",
"Cháo lòng":"Cháo lòng là món cháo được nấu theo phương thức nấu cháo thông thường, trong sự kết hợp với nước dùng ngọt làm từ xương lợn hay nước luộc lòng lợn, và nguyên liệu chính cho bát cháo không thể thiếu các món phủ tạng lợn luộc, dồi.",
"Cơm tấm":"Cơm tấm, cơm sườn, hay Cơm tấm Sài Gòn là một món ăn Việt Nam có nguyên liệu chủ yếu từ gạo tấm. Dù có nhiều tên gọi ở các vùng miền khác nhau, tuy nhiên nguyên liệu và cách thức chế biến của món ăn trên gần như là giống nhau.",
"Gói cuốn":"Gỏi cuốn hay còn được gọi là nem cuốn, là một món ăn khá phổ biến ở Việt Nam. Gỏi cuốn có xuất xứ từ Miền nam Việt Nam với tên gọi là gỏi cuốn - bằng các nguyên liệu gồm rau xà lách, húng quế, tía tô, tôm khô, rau thơm, thịt luộc, tôm tươi.. tất cả được cuộn trong vỏ bánh tráng",
"Hủ tiếu":"Hủ tiếu Nam Vang là một món ăn có có nguồn gốc từ Phnôm Pênh, Campuchia. Cộng đồng người Hoa ở Nam Vang (tên phiên âm Hán Việt của Phnôm Pênh) đã chế biến lại, sau đó đưa món ăn này về Việt Nam. Về sau, hủ tiếu Nam Vang được thêm nhiều loại gia vị đậm đà hơn để phù hợp với văn hóa ẩm thực của người Việt và trở thành đặc sản Sài Gòn, nổi tiếng ba miền. Hủ tiếu Nam Vang có thể ăn theo hai cách là khô và nước. Nguyên liệu chính sẽ bao gồm: hủ tiếu, gan heo, tôm, thịt bằm, rau sống và phần nước lèo thơm ngon. Món ăn này đã du nhập vào Việt Nam từ khá lâu và được rất nhiều người yêu thích.",
"Mì Quảng":"Mỳ Quảng là một món ăn đặc sản đặc trưng của Quảng Nam và Đà Nẵng, Việt Nam. Mỳ Quảng thường được làm từ bột gạo xay mịn với nước từ hạt dành dành và trứng cho có màu vàng và tráng thành từng lớp bánh mỏng, sau đó thái theo chiều ngang để có những sợi mỳ mỏng khoảng 5 -10mm.",
"Nem chua":"Nem là một trong những món ăn của người Việt, tùy theo địa phương có thể có các cách hiểu sau: Nem rán hay chả giò: là loại thức ăn bao gồm thịt xay, các loại rau, tôm, cua được cuốn bằng bánh đa nem phải rán chín mới ăn được với nước chấm.",
"Xôi xéo":"Xôi xéo là món xôi quen thuộc của người Hà Nội, mỗi khi nhắc tới là gợi đến ngay màu sắc vàng của xôi rất đặc trưng. Công đoạn nấu xôi xéo khá tốn nhiều thời gian từ việc chọn gạo nếp cho đến thành phẩm trưng bày. Cụ thể, người nấu phải chọn loại nếp cái hoa vàng thơm ngon, rồi ngâm với nước ấm khoảng 5 tiếng trước khi nấu xôi. Ngoài ra, chọn loại đậu xanh ruột vàng (bỏ vỏ), xay vỡ đôi hạt và cũng đem ngâm vào trong nước ấm chừng 2 tiếng rồi mới mang đi nấu chín kèm với ít muối. Sau khi đậu xanh chín, dùng đũa đánh tơi mịn và nắm chặt đậu thành từng nắm.",
"Phở":"Phở là một món ăn truyền thống của Việt Nam, có nguồn gốc từ Nam Định, Hà Nội và được xem là một trong những món ăn tiêu biểu cho nền ẩm thực Việt Nam. Thành phần chính của phở là bánh phở và nước dùng cùng với thịt bò hoặc thịt gà cắt lát mỏng. Thịt bò thích hợp nhất để nấu phở là thịt, xương từ các giống bò ta.",
"Gỏi cuốn":"Chẳng còn quá xa lạ với dân ghiền gỏi cuốn, món gỏi cuốn tôm thịt trứ danh với thịt ba chỉ, tôm tươi hoà quyện, khiến món gỏi trở nên thơm ngon khó cưỡng vô cùng. Gỏi cuốn tôm thịt với thịt thơm béo, tôm dai ngon ngọt tự nhiên còn có thêm bún tươi, rau sống, trứng chiên được cuộn trong một lớp bánh tráng mỏng vừa, chấm cùng tương đen, nước mắm chua ngọt hay thử các loại nước chấm gỏi cuốn đều ngon cả."}

def info():
    global thongtindoan, Label4

    wd2 = Toplevel()
    wd2.title('FOOD INFORMATION')
    wd2.iconbitmap('d:\\Downloads\\FoodRec\\lg2.ico')

    wd2.geometry('380x785+500+0')
    wd2.resizable(False, False)

    photo2 = ImageTk.PhotoImage(Image.open("d:\\Downloads\\FoodRec\\back.jpg"))
    Lbl2 = tk.Label(wd2, image=photo2)
    Lbl2.place(x = 0, y = 0)
    frame2 = Frame(wd2)
    frame2['bg'] = 'black'
    frame2['bd'] = 5
    frame2.place(x=11, y =43, width = 362 , height = 500)

    thongtindoan = tk.Message(wd2,width=358, bg= 'black',fg='white', justify= 'left', text= str(ham[prediction]), font=("Arial", 12))    
    thongtindoan.place(x = 11, y = 120)
    def translatethongtindoan():
        translator = Translator()
        translatetoen = translator.translate(ham[prediction], dest= 'en')
        thongtindoan_eng = Message(wd2, width=358, bg= 'black',fg='white', justify= 'left', text= str(translatetoen.text), font=("Arial", 12))  
        thongtindoan_eng.place(x = 11, y = 120)
    def backtowd1():
        wd2.destroy()
    backbutt = Button(wd2, text = '<', font=("", 13), bg = 'white', relief='flat', command= backtowd1)
    backbutt.place(x =15, y =50, width=20, height=20)

    #Nut translate
    Tranbutt = Button(wd2, text = 'Read in English 📝', bg = 'white', command=translatethongtindoan)
    Tranbutt.place(x = 260, y = 50)
        #dan cai QR
    photo = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\qrcode002.png"))
    label2 = tk.Label(wd2, image=photo)
    label2.image = photo
    label2.place(x = 150, y = 450)

    label3 = Label(wd2, text= "FOR MORE INFO", fg = 'black', bg='white', font=('Arial', 8))
    label3.place(x = 145, y = 428)

    #Product info label---------------------------------------------
    GLabel_4=tk.Label(wd2)
    GLabel_4['font'] = ("Arial", 5)
    GLabel_4["fg"] = "black"
    GLabel_4['bg'] = '#FDFDFD'
    GLabel_4["justify"] = "center"
    GLabel_4["text"] = "Designed by Dinh Khoi.\nBuilt using Python.\n🚫🔞📵"
    GLabel_4["relief"] = "flat"
    GLabel_4.place(x = 160, y = 750 )
    wd2.mainloop()


def close():
    tendoan.destroy()
    label2.destroy()
    label3.destroy()

def openandclose():
    load_img()
    GButton_208.config(state= ACTIVE)
    close()
    

def classify_once():
    global d
    try:
        classify()
        GButton_208['state'] = DISABLED
        infobutt['state'] = ACTIVE
        ytbutt['state'] = ACTIVE
        subpred['state'] = ACTIVE
    except NameError:
        messagebox.showerror("INPUT ERROR", 'No picture is found')

def youtube():
    webbrowser.open("https://www.youtube.com/results?search_query="+re.sub("\s", '+',prediction))


def sub_prediction():
    wd3 = Toplevel()
    wd3.title('OTHER PREDICTIONS')
    wd3.geometry("380x785+500+0")
    wd3.resizable(False, False)
    Label5 = tk.Label(wd3, image=photo1)
    Label5.place(x = 0, y = 0)

    frame3 = Frame(wd3)
    frame3['bg'] = 'black'
    frame3['bd'] = 5
    frame3.place(x=9, y =43, width = 363 , height = 500)
    img2 = ImageTk.PhotoImage(Image.open("d:\\Downloads\\FoodRec\\lo.png"))
    panel_image2 = tk.Label(frame3, image=img2).pack()
    #tao sub predict-------------------------------------------------
        #Top 5 lạ kì
    n = 5 #chạy top 5 kết quả predict
    y_preds = new_model.predict(image_batch)
    y_preds = np.argsort(y_preds, axis=1)[:,-n:]
    print(y_preds)
    #Đảo lại kết quả từ accuracy cao - thấp
    myorder = [4,3,2,1,0]
    y_preds = [[y_preds[0][m] for m in myorder]]
    print(y_preds)
    
    #hiển thị label top 5 kết quả
    y_predsforprinted = []
    i = 0
    for i in range(n):
        if y_preds[0][i] == 0:
            sub_prediction = 'Bánh bèo'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        if y_preds[0][i] == 1:
            sub_prediction = 'Bánh bột lọc'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        if y_preds[0][i] == 2:
            sub_prediction = 'Bánh căn' 
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        if y_preds[0][i] == 3:
            sub_prediction = 'Bánh canh'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        if y_preds[0][i] == 4:
            sub_prediction = 'Bánh chưng'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        if y_preds[0][i] == 5:
            sub_prediction = 'Bánh cuốn'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        if y_preds[0][i] == 6:
            sub_prediction = 'Bánh đúc' 
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        if y_preds[0][i] == 7:
            sub_prediction = 'Bánh giò'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)       
        if y_preds[0][i] == 8:
            sub_prediction = 'Bánh khọt'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        if y_preds[0][i] == 9:
            sub_prediction = 'Bánh mì'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)        
        if y_preds[0][i] == 10:
            sub_prediction = 'Bánh pía'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)        
        if y_preds[0][i] == 11:
            sub_prediction = 'Bánh tét' 
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)       
        if y_preds[0][i] == 12:
            sub_prediction = 'Bánh tráng nướng'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        if y_preds[0][i] == 13:
            sub_prediction = 'Bánh xèo'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        if y_preds[0][i] == 14:
            sub_prediction = 'Bún bò huế'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        if y_preds[0][i] == 15:
            sub_prediction = 'Bún đậu mắm tôm'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        if y_preds[0][i] == 16:
            sub_prediction = 'Bún mắm'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)       
        if y_preds[0][i] == 17:
            sub_prediction = 'Bún riêu' 
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)        
        if y_preds[0][i] == 18:
            sub_prediction = 'Bún thịt nướng' 
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)         
        if y_preds[0][i] == 19:
            sub_prediction = 'Cá kho tộ'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)       
        if y_preds[0][i] == 20:
            sub_prediction = 'Canh chua'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)       
        if y_preds[0][i] == 21:
            sub_prediction = 'Cao lầu' 
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)      
        if y_preds[0][i] == 22:
            sub_prediction = 'Cháo lòng'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)       
        if y_preds[0][i] == 23:
            sub_prediction = 'Cơm tấm'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)       
        if y_preds[0][i] == 24:
            sub_prediction = 'Gỏi cuốn'    
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)        
        if y_preds[0][i] == 25:
            sub_prediction = 'Hủ tiếu'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)        
        if y_preds[0][i] == 26:
            sub_prediction = 'Mì Quảng'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)      
        if y_preds[0][i] == 27:
            sub_prediction = 'Nem chua'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)       
        if y_preds[0][i] == 28:
            sub_prediction = 'Phở'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)        
        if y_preds[0][i] == 29:
            sub_prediction = 'Xôi xéo'
            print(sub_prediction)
            y_predsforprinted.append(sub_prediction)
        
    print(y_predsforprinted)
    #Cac nut dai dien
    label_otherchoices = Label(wd3, text= 'These are top 4 predictions: ',font=("Arial", 12), fg = 'midnightblue', bg = 'white')
    label_otherchoices.place(x= 20, y = 550)

    def other_choices_command1():
        webbrowser.open('https://www.google.com/search?&q='+re.sub("\s+","+",y_predsforprinted[1])+' là+gì+?')
    def other_choices_command2():
        webbrowser.open('https://www.google.com/search?&q='+re.sub("\s+","+",y_predsforprinted[2])+' là+gì+?')
    def other_choices_command3():
        webbrowser.open('https://www.google.com/search?&q='+re.sub("\s+","+",y_predsforprinted[3])+' là+gì+?')
    def other_choices_command4():
        webbrowser.open('https://www.google.com/search?&q='+re.sub("\s+","+",y_predsforprinted[4])+' là+gì+?')
    
    ansno2 = Button(wd3,  text = y_predsforprinted[1], command=other_choices_command1, font= ("Arial", 12), bg= '#2E86C1')
    ansno2.place(x = 95, y= 580,width= 200, height= 30)

    ansno3 = Button(wd3, text = y_predsforprinted[2],command=other_choices_command2, font= ("Arial", 12), bg= '#3498DB' )
    ansno3.place(x = 95, y= 620,width= 200, height= 30 )
    
    ansno4 = Button(wd3, text = y_predsforprinted[3],command=other_choices_command3, font= ("Arial", 12), bg= '#5DADE2' )
    ansno4.place(x = 95, y= 660,width= 200, height= 30 )

    ansno5 = Button(wd3, text = y_predsforprinted[4],command=other_choices_command4, font= ("Arial", 12), bg= '#85C1E9' )
    ansno5.place(x = 95, y= 700,width= 200, height= 30 )

    def backtowd31():
        wd3.destroy()
    backbutt = Button(wd3, text = '<', font=("", 13), bg = 'white', relief='flat', command= backtowd31)
    backbutt.place(x =15, y =50, width=20, height=20)

    GLabel_5=tk.Label(wd3)
    GLabel_5['font'] = ("Arial", 5)
    GLabel_5["fg"] = "black"
    GLabel_5['bg'] = '#FDFDFD'
    GLabel_5["justify"] = "center"
    GLabel_5["text"] = "Designed by Dinh Khoi.\nBuilt using Python.\n🚫🔞📵"
    GLabel_5["relief"] = "flat"
    GLabel_5.place(x = 160, y = 750 )
    wd3.mainloop()
#WINDOW1-------------------------------------------------------------------
wd = Tk()
wd.title('TENSORFLOW 30 VIETNAM FOOD RECOGNITION')
wd.iconbitmap('d:\\Downloads\\FoodRec\\lg2.ico')

wd.geometry('380x785+500+0')
wd.resizable(False, False)

photo1 = ImageTk.PhotoImage(Image.open("d:\\Downloads\\FoodRec\\back.jpg"))
Label1 = tk.Label(wd, image=photo1)
Label1.place(x = 0, y = 0)

#Button Open
GButton_991=tk.Button(wd)
GButton_991["bg"] = "#3498DB"
GButton_991['font'] = ("", 10)
GButton_991["fg"] = "#000000"
GButton_991["justify"] = "center"
GButton_991["text"] = "IMAGE OPEN"
GButton_991.place(x=40 ,y=730,width=155,height=40)
GButton_991["command"] = openandclose

#Button classify
GButton_208=tk.Button(wd)
GButton_208["bg"] = "#154360"
GButton_208['font'] = ("", 10)
GButton_208["fg"] = "white"
GButton_208["justify"] = "center"
GButton_208["text"] = "CLASSIFY"
GButton_208.place(x=195,y=730,width=155,height=40)
GButton_208["command"] = classify_once

#Button INFO
infobutt=tk.Button(wd)
infobutt["bg"] = "#D4E6F1"
infobutt['font'] = ("", 10)
infobutt["fg"] = "black"
infobutt["justify"] = "center"
infobutt["text"] = "INFO"
infobutt.place(x=40,y=650,width=70,height=70)
infobutt["command"] = info
infobutt['relief'] = 'flat'
infobutt['state'] = DISABLED

#Button YOUTUBE
photo_yt = ImageTk.PhotoImage(Image.open("d:\\Downloads\\FoodRec\\yt.png"))
ytbutt=tk.Button(wd)
ytbutt["image"] = photo_yt
ytbutt.place(x=160,y=650,width=70,height=70)
ytbutt["command"] = youtube
ytbutt['state'] = DISABLED

#Button Subprediction
subpred=tk.Button(wd)
subpred["bg"] = "#AED6F1"
subpred['font'] = ("", 10)
subpred["fg"] = "black"
subpred["justify"] = "center"
subpred["text"] = "MORE \n ANSWER"
subpred.place(x=280,y=650,width=70,height=70)
subpred["command"] = sub_prediction
subpred['relief'] = 'flat'
subpred['state'] = DISABLED

#Frame goi hinh
frame = Frame(wd)
frame['bg'] = 'whitesmoke'
frame['bd'] = 5
frame.place(x=11, y =43, width = 361 , height = 500)

wd.mainloop()

