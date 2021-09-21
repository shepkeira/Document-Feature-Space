import os
import re
from calculating_metrics import calculate_metrics
from processing import process_file

# input: directory_path you want file from
# output: list of all files in a directory
def get_file_names(directory_path):
    files = os.listdir(directory_path)
    return files

# input: file name to get contents from
# output: all content of the articles into one string variable
def read_file(file_name):
    with open(file_name, 'r', encoding="utf8") as f:
        file_contents = f.read()
        return file_contents

# input: file_name you want to read contents for
# output: the contents of a file in an array of sentences which are arrays of words
def read_processed_file(file_name):
    file_contents = []
    with open(file_name, 'r', encoding="utf8") as f:
        myline = f.readline()
        while myline:
            myline = re.sub('\n', '', myline)
            file_line_array = re.split(' ', myline)
            file_contents.append(file_line_array)
            myline = f.readline()
    return file_contents

# input: contents of a file in an array of sentences which are arrays of words; file_name you want to write to
# output: nothing
# this function writes contents of a proccessed file into a new file under "processed_articles"
def write_contents_to_file(contents, file_name):
    phrases = []
    for phrase_array in contents:
        phrases.append(' '.join(phrase_array))
    file_contents = "\n".join(phrases)
    path = os.path.join(os.getcwd(), "processed_articles", file_name)
    f = open(path, 'w')
    f.write(file_contents)
    f.close()

# input: nothing
# output: a dictionary of file_names: processed article contents
def get_processed_file_contents():
    processed_articles_path = os.path.join(os.getcwd(), "processed_articles")
    if os.path.exists(processed_articles_path):
        file_names = get_file_names(processed_articles_path)
        files_contents = {}
        for file_name in file_names:
            article_path = os.path.join(processed_articles_path, file_name)
            files_contents[file_name] = read_processed_file(article_path)
        return files_contents
    else:
        print("There was an error.")
        return 0

# input: nothing
# output: dictionary of file_names: file_content_strings from the articles folder
def get_file_contents():
    articles_path = os.path.join(os.getcwd(), "articles")
    if os.path.exists(articles_path):
        file_names = get_file_names(articles_path)
        files_contents = {}
        for file_name in file_names:
            article_path = os.path.join(articles_path, file_name)
            files_contents[file_name] = read_file(article_path)
        return files_contents
    else:
        print("Articles are not found.")
        return 0

def write_metrics_to_file(all_metrics):
    file_contents = ""
    for file_name, metrics in all_metrics.items():
        file_contents += file_name + ": " + (' ').join(map(str, metrics)) + "\n"
    path = os.path.join(os.getcwd(), "metrics", "final_metrics")
    f = open(path, 'w')
    f.write(file_contents)
    f.close()

def main():
    # Read in data
    files_contents = get_file_contents()
    if files_contents == 0:
        print("There was an error. Please confirm that the files are located in /articles.")
    # Process files
    for file_name, file_contents in files_contents.items():
        # Process Your Files
        processed_contents = process_file(file_contents)
        # Write The Contents Of The Processed Files to new Files
        write_contents_to_file(processed_contents, file_name)

    # Retrieve the Processed Files
    proccessed_files_contents = get_processed_file_contents()
    all_metrics = {}
    for file_name, file_contents in proccessed_files_contents.items():
        # Calculate the metrics for each file
        # order of metrics:
        # - total # words
        # - max # syllabls per word
        # - min # syllabls per word
        # - avg # syllable per word
        # - total # sentences
        # - max # words / sentence
        # - min # words / sentence
        # - avg # words / sentene
        # - flesch reading ease score
        metrics = calculate_metrics(file_contents)
        # display metrics and the files associated with each
        all_metrics[file_name] = metrics
    write_metrics_to_file(all_metrics)

# runs main to start
if __name__ == "__main__":
    main()
