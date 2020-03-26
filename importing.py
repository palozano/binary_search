import urllib.request
import tempfile
import shutil
import gzip
import csv


def main():
    """Script entry point."""

    file_names = "names.txt"
    file_names_sorted = "sorted_names.txt"

    print('Fetching data from IMDb...')

    with open(file_names, encoding="utf-8", mode="w") as destination:
        destination.writelines(names())

    with open(file_names, encoding="utf-8") as source,\
            open(file_names_sorted, encoding="utf-8", mode="w") as destination:
        destination.writelines(sorted(source.readlines()))

    print("Created {} and {}!".format(file_names, file_names_sorted))


def names():
    """Return a generator of names with a trailing newline"""

    url = 'https://datasets.imdbws.com/name.basics.tsv.gz'

    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(mode="w+b") as archive:
            print('Beginning file download...')
            shutil.copyfileobj(response, archive)
            print("Done!")
            archive.seek(0)
            print("Decompressing...")
            with gzip.open(archive, mode="rt", encoding="utf-8") as tsv_file:
                tsv = csv.reader(tsv_file, delimiter="\t")
                next(tsv)  # Skip the header
                for record in tsv:
                    full_name = record[1]
                    yield "{}\n".format(full_name)
                print("Done!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted")
