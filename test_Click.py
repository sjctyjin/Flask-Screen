import tkinter

import tkinter.filedialog

import os

from PIL import ImageGrab

from time import sleep

# 創建tkinter主窗口

root = tkinter.Tk()

# 指定主窗口位置與大小

root.geometry('100x40+400+300')

# 不允許改變窗口大小

root.resizable(False, False)


class MyCapture:

    def __init__(self, png):

        # 變量X和Y用來記錄滑鼠左鍵按下的位置

        self.X = tkinter.IntVar(value=0)

        self.Y = tkinter.IntVar(value=0)

        # 屏幕尺寸

        screenWidth = root.winfo_screenwidth()

        screenHeight = root.winfo_screenheight()

        # 創建頂級組件容器

        self.top = tkinter.Toplevel(root, width=screenWidth, height=screenHeight)

        # 不顯示最大化、最小化按鈕

        self.top.overrideredirect(True)

        self.canvas = tkinter.Canvas(self.top, bg='white', width=screenWidth, height=screenHeight)

        # 顯示全屏截圖，在全屏截圖上進行區域截圖

        self.image = tkinter.PhotoImage(file=png)

        self.canvas.create_image(screenWidth // 2, screenHeight // 2, image=self.image)

        # 滑鼠左鍵按下的位置

        def onLeftButtonDown(event):

            self.X.set(event.x)

            self.Y.set(event.y)

            # 開始截圖

            self.sel = True

        self.canvas.bind('<Button-1>', onLeftButtonDown)

        # 滑鼠左鍵移動，顯示選取的區域

        def onLeftButtonMove(event):

            if not self.sel:
                return

            global lastDraw

            try:

                # 刪除剛畫完的圖形，要不然滑鼠移動的時候是黑乎乎的一片矩形

                self.canvas.delete(lastDraw)

            except Exception as e:

                pass

            lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='black')

        self.canvas.bind('<B1-Motion>', onLeftButtonMove)

        # 獲取滑鼠左鍵擡起的位置，保存區域截圖

        def onLeftButtonUp(event):

            self.sel = False

            try:

                self.canvas.delete(lastDraw)

            except Exception as e:

                pass

            sleep(0.1)

            # 考慮滑鼠左鍵從右下方按下而從左上方擡起的截圖

            left, right = sorted([self.X.get(), event.x])

            top, bottom = sorted([self.Y.get(), event.y])

            pic = ImageGrab.grab((left + 1, top + 1, right, bottom))

            # 彈出保存截圖對話框

            fileName = tkinter.filedialog.asksaveasfilename(title='保存截圖', filetypes=[('JPG files', '*.jpg')])

            if fileName:
                pic.save(fileName + '.jpg')

            # 關閉當前窗口

            self.top.destroy()

        self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp)

        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    # 開始截圖


def buttonCaptureClick():
    # 最小化主窗口

    root.state('icon')

    sleep(0.2)

    filename = 'temp.png'

    im = ImageGrab.grab()

    im.save(filename)

    im.close()

    # 顯示全屏幕截圖

    w = MyCapture(filename)

    buttonCapture.wait_window(w.top)

    # 截圖結束，恢復主窗口，並刪除臨時的全屏幕截圖文件

    root.state('normal')

    os.remove(filename)


buttonCapture = tkinter.Button(root, text='截圖', command=buttonCaptureClick)

buttonCapture.place(x=10, y=10, width=80, height=20)

# 啓動消息主循環

root.mainloop()