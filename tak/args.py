from argparse import ArgumentParser
from glob import glob
from PIL import Image

parser=ArgumentParser(description='zmiana jpeg na czarno białe')
parser.add_argument(
    '--input',help="folder z którego pobieram obrazy",required=True)
parser.add_argument(
    '--output',help="folder do którego zapisze obrazy",required=True)
args=parser.parse_args()
print(args)
print(args.input,args.output)
for path in glob(args.input+'/*'):
    directory,filename=path.split('\\')
    print(path,directory,filename)
    with Image.open(path) as new_image:
        czarnobialy=new_image.convert('L')
        czarnobialy.save(args.output+'/'+filename)
        zmniejszony=new_image.resize((128,128))
        zmniejszony.save(args.output+"/min_"+filename)
        obrot=new_image.rotate(45)
        obrot.save(args.output+"/obrot_"+filename)
        gora=new_image.transpose(Image.FLIP_TOP_BOTTOM)
        gora.save(args.output+"/flip_"+filename)
