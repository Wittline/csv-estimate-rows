import mmap
import os

class Csvnrows(object):    

    @staticmethod
    def estimate_csv_rows(filename, header = True):

        count_records = 0

        with open(filename, mode="r", encoding = "ISO-8859-1") as file_obj:

            with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as map_file:

                buffer = map_file.read(1<<13)
                file_size = os.path.getsize(filename)
                count_records = file_size // (len(buffer) // buffer.count(b'\n')) - (1 if header else 0)                

        return count_records

print(estimate_csv_rows('/content/csvData.csv'))
