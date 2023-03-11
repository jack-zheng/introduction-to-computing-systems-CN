import os
import fitz

'''
Steps:
    1. 输入目标页 e.g. 1,3 从第一页开始到第三页(包含)
    2. 根据页码生成提取文字并存入文件中
        * 每一页内容前面都需要有页码标识
'''

def extra_chi(file, from_page, to_page):
    doc = fitz.open(file)
    output_name = "page%s-%s.txt" % (from_page, to_page)
    with open(output_name, "w") as file:
        for num in range(from_page, to_page + 1):
            print("Processing page %s..." %(num))
            # 提取当前页面中文
            page = doc[num]
            tpage = page.get_textpage_ocr(language="chi_sim", dpi=300)
            txt = tpage.extractText()
            
            # 去除文字间多余的空格
            lines = txt.split('\n')
            no_space = []

            for line in lines:
                words = line.split()
                tmp = "".join(words)
                no_space.append(tmp)
            
            # 解析结果写入文件
            file.write("--- page %s start ---\n" %(num))
            file.write("".join(no_space))
            file.write("--- page %s end ---\n" %(num))

if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    from_page = int(sys.argv[2])
    to_page = int(sys.argv[3])
    print("Start extract book %s from page %s to page %s..." %(path, from_page, to_page))
    extra_chi(path, from_page, to_page)
    print("Finish extract...")