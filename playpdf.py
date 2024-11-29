"""
处理pdf文件
"""
import os
import fitz
from fitz import Document, Page, Pixmap
from tqdm import tqdm


class pdf2pic:
    def __init__(self, folder:str=None, file:str=None, zoom_x:float=3, zoom_y:float=3):
        """

        :param folder: pdf所在文件夹
        :param file: pdf文件名
        :param zoom_x: x方向缩放系数 默认 1.33
        :param zoom_y: y方向缩放系数 默认 1.33
        """
        self.folder = folder
        self.file = file
        self.zoom_x = zoom_x
        self.zoom_y = zoom_y

    def pdf2pic_folder(self):
        """
        用于把整个文件夹中的pdf文件全部转为图片
        :return:
        """
        image_folder:str = f'{self.folder}pic'  # 用于存放图片的文件夹，若pdf文件夹为D:\temp\pdf，则生成图片文件夹为D:\temp\pdfpic
        if not os.path.exists(image_folder):  # 如果文件夹不存在就创建文件夹
            os.makedirs(image_folder)
        dir0:list = os.listdir(self.folder)  # 遍历pdf所在文件夹
        for pdf in tqdm(dir0, desc='进度'):  # 遍历文件夹中的每个文件
            # pdf:str 文件名
            file:str = os.path.join(self.folder, pdf)  # 生成单个pdf路径
            # 防止文件夹中有非pdf文件，加了try语句
            try:
                pdf_object:Document = fitz.open(file)
            except:
                print(f'无法打开{file}')
                continue
            for pg in range(0, pdf_object.page_count):  # 遍历pdf文件的每一页
                page:Page = pdf_object[pg]  # 获取某一页
                mat = fitz.Matrix(self.zoom_x, self.zoom_y)  # 定义图片的缩放比例
                pic:Pixmap = page.get_pixmap(matrix=mat, dpi=None, colorspace='rgb', alpha=False)  # 获取图片
                image_name:str = os.path.join(image_folder, pdf)  # 定义图片名称的一部分
                pic.save(f'{image_name}_{pg}.jpg')

    def pdf2pic_file(self):
        """
        用于把单个pdf文件每页导出为图片
        :return:
        """
        pdf_object: Document = fitz.open(self.file)
        for pg in range(0, pdf_object.page_count):
            page: Page = pdf_object[pg]
            mat = fitz.Matrix(self.zoom_x, self.zoom_y)
            pic: Pixmap = page.get_pixmap(matrix=mat, dpi=None, colorspace='rgb', alpha=False)
            pic.save(f'{self.file}_{pg}.jpg')


if __name__ == '__main__':
    folder1: str = r'D:\工作及项目\2024年工作及项目\2024.00 吾通\财务工作\2024年11月报销\00-无项目\已记账'
    pdf2pic1 = pdf2pic(folder1)
    pdf2pic1.pdf2pic_folder()