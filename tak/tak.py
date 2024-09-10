from PIL import Image
import pathlib
jpgs=pathlib.Path("kolorowe").glob("*.jpg")
for path in jpgs:
    new_name=str(path).split("//")[2].split(".")[0]+"_modified.jpg"
    print(new_name)
    with Image.open(path) as image:
        print(image.size)
        width,height=image.size
        if width>1000 and height>1000:
            out=image.resize((int(0.4*width), int(0.4*height)))
            out.save(pathlib.Path(f"kolorowe/{new_name}"),"JPG")