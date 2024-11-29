"""用于将doc/docx格式文件批量转换为pdf格式文件"""
from win32com import client as wc
import os

print('用    途：用于将指定文件夹下的多个word文件批量转换为pdf文件，支持doc及docx格式。')
print('#############################################################################')
word=wc.Dispatch('Word.Application')
print('提    示：1、文件夹中只能有word文件；')
print('         2、本窗口若不能粘贴请百度改命令提示符窗口属性设置；')
filewd=input('在此处输入或粘贴word文件所在文件夹路径后按下Enter键:')
filewd_pdf=filewd+'pdf'
print('转换后的pdf文件将存储于： '+filewd_pdf)

i=os.path.exists(filewd_pdf)
if not i:
    os.makedirs(filewd_pdf)

dirlist=os.listdir(filewd)
for filename in dirlist:
    doc=word.Documents.Open(filewd+'\\'+filename)        # 目标路径下的文件
    if 'docx' not in filename:
        pdf=filewd_pdf+'\\'+filename.replace('doc','pdf')
    else:
        pdf=filewd_pdf+'\\'+filename.replace('docx','pdf')
    doc.SaveAs(pdf, 17, False, "", True, "", False, False, False, False)  # 转化后路径下的文件    
    doc.Save()
    doc.Close()
    #word.Quit()  加上这条会报错
    print(filename+'  转换pdf成功！')

input('按下Enter键退出：')

