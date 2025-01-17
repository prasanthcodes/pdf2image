
import os
# from pdf2image import convert_from_path

# folder_names=[]
# pdf_names=os.listdir('input_dir')

# for i in range(len(pdf_names)):
    # pdf_name=pdf_names[i]
    # pdf_path='input_dir'+os.sep+pdf_name
    # pages = convert_from_path(pdf_path, 400,poppler_path=r'c:/poppler-0.68.0/bin')

    # out_folder=pdf_name.split('.')[0]
    # for count, page in enumerate(pages):
        # page.save(out_folder+os.sep+f'out{count}.jpg', 'JPEG')
        
        
        
import ghostscript
import locale

def pdf2jpeg(pdf_input_path, jpeg_output_path):
    """
    Source: https://stackoverflow.com/questions/60701262/convert-pdf-to-image-using-python, 
    https://www.kite.com/python/answers/how-to-remove-everything-after-a-character-in-a-string-in-python, 
    https://www.ghostscript.com/doc/current/Use.htm
    """
    args = ["pdf2jpeg", # actual value doesn't matter
            "-dNOPAUSE",
            "-sDEVICE=jpeg",
            "-r444",
            "-sOutputFile=" + jpeg_output_path.split(".", 1)[0] + "-%d.jpg",
            pdf_input_path]

    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]

    ghostscript.Ghostscript(*args)
    
    
folder_names=[]
pdf_names=os.listdir('input_dir')

for i in range(len(pdf_names)):
    pdf_name=pdf_names[i]
    pdf_path='input_dir'+os.sep+pdf_name
    
    #out_folder=pdf_name.split('.')[0]
    out_folder='out'
    jpeg_output_path=out_folder+os.sep+f'out'
    pdf2jpeg(pdf_path,jpeg_output_path)
    
    