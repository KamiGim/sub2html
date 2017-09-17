import os

src_folder = "./subtitles"
res_folder = "./results"

if not os.path.exists(res_folder):
    os.makedirs(res_folder)

for file in os.listdir(src_folder):
    print("open file : " + file);
    filepath = os.path.join(src_folder, file);
    res_file_name = os.path.splitext(file)[0] + ".html";
    res_file_path = os.path.join(res_folder, res_file_name);

    res_file = open(res_file_path, 'w', encoding="utf8");
    with open(filepath, 'r', encoding="utf8") as f:
        for line in f:
            if not line[0].isdigit():
                newLine = line + "<br />";
                res_file.write(newLine);
    print("successfully write file : " + res_file_path);
    # f.close()
