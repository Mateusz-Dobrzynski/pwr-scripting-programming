import argparse
from os import path, listdir
from time import ctime
import magic
from hashlib import md5, sha256
from PIL import ExifTags, Image

files_list = []

full_report = "# Report\n"


def write_to_report(text: str):
    global full_report
    full_report = f"{full_report}\n{text}"


def main():
    parser = construct_argument_parser()
    args = parser.parse_args()
    if not args.directory:
        write_to_report("Please define target directory")
        return 1
    if not args.output:
        write_to_report("Please define output report path")
        return 1
    output = args.output
    directory = path.dirname(args.directory)

    write_to_report("## Directory tree\n")

    write_to_report("```")
    draw_directory_tree(directory)
    write_to_report("```")

    write_to_report("\n## Detailed file analysis\n")
    for file in files_list:
        analyze(file)

    output_file = open(output, "w")
    output_file.write(full_report)
    output_file.close()

    sha_digest = sha256(bytes(full_report, "utf-8")).hexdigest()
    md5_digest = md5(bytes(full_report, "utf-8")).hexdigest()
    digest_report = open(f"{output}_digest.txt", "w")
    digest_report.write(f"SHA: {sha_digest}\nMD5: {md5_digest}")
    digest_report.close()


def construct_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Directory to traverse")
    parser.add_argument("-o", "--output", help="Output report path")
    return parser


def draw_directory_tree(directory, indentations_count=0):
    indentations = indentations_count * " " * 4
    write_to_report(f"{indentations}{directory.split('/')[-1]}")
    for entry in listdir(directory):
        full_path = path.join(directory, entry)
        if path.isdir(full_path):
            draw_directory_tree(full_path, indentations_count + 1)
        else:
            write_to_report(f"{indentations}    {entry}")
            files_list.append(full_path)


def analyze(file_path: str):
    write_to_report(f"`{file_path}`")
    write_to_report(f"\t{magic.from_file(file_path)}")
    file = open(file_path, "rb")
    content = file.read()
    file.close()
    last_changed = ctime(path.getctime(file_path))
    last_accessed = ctime(path.getatime(file_path))
    write_to_report(f"\tLast changed: {last_changed}")
    write_to_report(f"\tLast accessed: {last_accessed}")
    write_to_report(f"\tSHA256: {sha256(content).hexdigest()}")
    write_to_report(f"\tMD5: {md5(content).hexdigest()}")
    if file_path.endswith((".jpg", ".png", ".jpeg")):
        im = Image.open(file_path)
        exif = im.getexif()
        gps_ifd = exif.get_ifd(ExifTags.IFD.GPSInfo)
        latitude = gps_ifd[2]
        latitudeRef = gps_ifd[1]
        longitude = gps_ifd[4]
        longitudeRef = gps_ifd[3]
        write_to_report(
            f"\tCoordinates: {latitude[0]}° {latitude[1]}′ {latitude[2]}” {latitudeRef}, {longitude[0]}° {longitude[1]}′ {longitude[2]}” {longitudeRef}"
        )


if __name__ == "__main__":
    main()
